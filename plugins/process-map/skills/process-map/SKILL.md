---
name: process-map
description: Map a business's processes department by department (steps, owners, status, monthly time, tool costs) into a YAML file and render it as an HTML page with a diagram and cost totals. Use when the user wants to map, document or audit processes, find what to automate, or estimate the cost of a workflow.
---

# Process map

The map is one YAML file. `example.yaml` next to this file is the format; copy its
shape. Each step has `id`, `name`, `owner`, `status` (`live` | `testing` | `idea`),
`minutes_per_month`, `tools` (`name`, monthly `cost`), `next` (ids of following
steps) and optional `instructions`.

1. **Collect.** Read the docs or code the user points to, or interview them one
   department at a time: what happens, who does it, how often, how long, with which
   tools. Ask for numbers; when the user guesses, write the guess and add
   `# stima` next to it. Never invent numbers.
2. **Write** the YAML in the project (default `docs/process-map.yaml`). No client
   names or personal data in maps that will be published.
3. **Render:** `uv run ${CLAUDE_PLUGIN_ROOT}/skills/process-map/render.py <map.yaml>`.
   It validates ids, statuses and `next` links, and writes `<map>.html` next to it.
4. **Report** in a few lines: monthly total, the most expensive department, and the
   three `live` steps with the highest labour cost as automation candidates.
