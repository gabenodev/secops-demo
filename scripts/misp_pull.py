"""Pull IP indicators from MISP into the Logstash lookup file (RISK-REGISTER R-04).

Feed lifecycle in one place: only attributes flagged to_ids (trust), minus
anything on a MISP warninglist (known benign), seen within MISP_MAX_AGE
(ageing out), one line per IP (deduplicated), sorted so diffs stay small.
"""
import json
import os
import re
import sys
import time
from pathlib import Path

OUT = Path("enrich/ioc_ip.yml")

_AGE = re.compile(r"^(\d+)([dhms])$", re.I)
_UNITS = {"s": 1, "m": 60, "h": 3600, "d": 86400}


def resolve_max_age(raw: str) -> int | str:
    """Turn MISP_MAX_AGE into a unix cutoff.

    Some MISP builds ignore relative strings like ``30d`` and return nothing;
    an absolute unix timestamp is reliable (R-04).
    """
    raw = (raw or "30d").strip()
    if raw.isdigit():
        return int(raw)
    m = _AGE.match(raw)
    if not m:
        return raw
    return int(time.time()) - int(m.group(1)) * _UNITS[m.group(2).lower()]


def render(attrs):
    """Return the translate dictionary: one "ip": "misp:<event>:<category>" line per IP."""
    seen = {}
    for a in attrs:
        seen.setdefault(a.value, f"misp:{a.event_id}:{a.category}")
    return "".join(f"{json.dumps(ip)}: {json.dumps(tag)}\n" for ip, tag in sorted(seen.items()))


def main():
    import pymisp

    misp = pymisp.PyMISP(
        os.environ["MISP_URL"], os.environ["MISP_KEY"], ssl=os.environ.get("MISP_CA") or False
    )
    attrs = misp.search(
        controller="attributes",
        type_attribute=["ip-dst", "ip-src"],
        to_ids=True,
        enforce_warninglist=True,
        timestamp=resolve_max_age(os.environ.get("MISP_MAX_AGE", "30d")),
        pythonify=True,
    )
    text = render(attrs)
    if not text:
        sys.exit("MISP returned no indicators; the previous lookup file stays in place.")
    OUT.parent.mkdir(exist_ok=True)
    tmp = OUT.with_suffix(".tmp")
    tmp.write_text(text)
    tmp.replace(OUT)  # atomic, so Logstash never reads a half-written file
    print(f"{len(text.splitlines())} unique indicators written to {OUT}")


if __name__ == "__main__":
    main()
