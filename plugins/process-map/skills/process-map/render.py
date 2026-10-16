# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Render a process map YAML into a single HTML page: Mermaid diagram + cost totals.

Usage: uv run render.py map.yaml [out.html]
"""
import html
import sys
from pathlib import Path

import yaml

STATUSES = ("live", "testing", "idea")


def load(path):
    data = yaml.safe_load(Path(path).read_text())
    ids = [s["id"] for d in data["departments"] for s in d["steps"]]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        sys.exit(f"duplicate step ids: {sorted(dupes)}")
    for d in data["departments"]:
        for s in d["steps"]:
            if s.get("status", "idea") not in STATUSES:
                sys.exit(f"{s['id']}: status must be one of {STATUSES}")
            for n in s.get("next", []):
                if n not in ids:
                    sys.exit(f"{s['id']}: next '{n}' is not a step id")
    return data


def tool_costs(steps):
    # A tool used by several steps is paid once: dedupe by name, keep the highest cost seen.
    tools = {}
    for s in steps:
        for t in s.get("tools", []):
            tools[t["name"]] = max(tools.get(t["name"], 0), t.get("cost", 0))
    return tools


def labor(steps, rate):
    return sum(s.get("minutes_per_month", 0) for s in steps) / 60 * rate


def totals(data):
    rate = data.get("hourly_rate", 0)
    rows = []
    for d in data["departments"]:
        rows.append((d["name"], labor(d["steps"], rate), sum(tool_costs(d["steps"]).values())))
    every = [s for d in data["departments"] for s in d["steps"]]
    return rows, (labor(every, rate), sum(tool_costs(every).values()))


def mermaid(data):
    q = lambda t: str(t).replace('"', "#quot;")
    lines = ["flowchart LR"]
    for i, d in enumerate(data["departments"]):
        lines.append(f'  subgraph dept{i}["{q(d["name"])}"]')
        for s in d["steps"]:
            lines.append(f'    {s["id"]}["{q(s["name"])}"]:::{s.get("status", "idea")}')
        lines.append("  end")
    for d in data["departments"]:
        for s in d["steps"]:
            lines += [f'  {s["id"]} --> {n}' for n in s.get("next", [])]
            lines.append(f'  click {s["id"]} href "#{s["id"]}"')
    lines += [
        "  classDef live fill:#d1fadf,stroke:#12b76a",
        "  classDef testing fill:#fef0c7,stroke:#f79009",
        "  classDef idea fill:#f2f4f7,stroke:#98a2b3,stroke-dasharray:4",
    ]
    return "\n".join(lines)


def render(data):
    cur = data.get("currency", "EUR")
    money = lambda v: f"{v:,.0f} {cur}"
    e = lambda v: html.escape(str(v))
    rows, (lab, tools) = totals(data)
    summary = "".join(
        f"<tr><td>{e(n)}</td><td>{money(l)}</td><td>{money(t)}</td><td>{money(l + t)}</td></tr>"
        for n, l, t in rows
    )
    summary += f"<tr class=total><td>Totale</td><td>{money(lab)}</td><td>{money(tools)}</td><td>{money(lab + tools)}</td></tr>"
    rate = data.get("hourly_rate", 0)
    steps = "".join(
        f"<tr id={e(s['id'])}><td>{e(d['name'])}</td><td><b>{e(s['name'])}</b><br><small>{e(s.get('instructions', ''))}</small></td>"
        f"<td>{e(s.get('owner', ''))}</td><td><span class={e(s.get('status', 'idea'))}>{e(s.get('status', 'idea'))}</span></td>"
        f"<td>{money(s.get('minutes_per_month', 0) / 60 * rate)}</td>"
        f"<td>{e(', '.join(t['name'] for t in s.get('tools', [])))}</td></tr>"
        for d in data["departments"]
        for s in d["steps"]
    )
    return f"""<!doctype html><html lang=it><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>{e(data['name'])}</title>
<style>
body{{font:15px/1.5 system-ui,sans-serif;max-width:1100px;margin:auto;padding:16px;background:#fff;color:#101828}}
table{{border-collapse:collapse;width:100%;margin:16px 0}}td,th{{border-bottom:1px solid #eaecf0;padding:6px 8px;text-align:left;vertical-align:top}}
.total{{font-weight:600}}.live,.testing,.idea{{padding:1px 8px;border-radius:9px;font-size:12px}}
.live{{background:#d1fadf}}.testing{{background:#fef0c7}}.idea{{background:#f2f4f7}}
tr:target{{background:#eff8ff}}.wrap{{overflow-x:auto}}
</style>
<h1>{e(data['name'])}</h1>
<p>Costo orario: {money(rate)} · costi mensili</p>
<div class=wrap><pre class=mermaid>{html.escape(mermaid(data), quote=False)}</pre></div>
<h2>Costi per reparto</h2>
<div class=wrap><table><tr><th>Reparto</th><th>Lavoro</th><th>Tool</th><th>Totale</th></tr>{summary}</table></div>
<h2>Passaggi</h2>
<div class=wrap><table><tr><th>Reparto</th><th>Passaggio</th><th>Owner</th><th>Stato</th><th>Lavoro</th><th>Tool</th></tr>{steps}</table></div>
<script type=module>
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";
mermaid.initialize({{startOnLoad:true,securityLevel:"loose"}});
</script></html>
"""


if __name__ == "__main__":
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".html")
    out.write_text(render(load(src)))
    print(out)
