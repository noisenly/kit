# /// script
# dependencies = ["pyyaml"]
# ///
"""Self-check: uv run test_render.py"""
from pathlib import Path

from render import load, render, totals

data = load(Path(__file__).with_name("example.yaml"))
rows, (lab, tools) = totals(data)
assert rows[0] == ("Vendite", (180 + 600 + 480) / 60 * 40, 29 + 20), rows[0]  # HubSpot paid once
assert lab == (180 + 600 + 480 + 240 + 120) / 60 * 40, lab
assert tools == 29 + 20 + 10 + 30, tools
page = render(data)
assert 'click lead-intake href "#lead-intake"' in page and "<tr id=invoice>" in page
print("ok")
