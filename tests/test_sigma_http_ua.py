"""Detection as code for the odd HTTP user-agent rule (RISK-REGISTER R-03)."""
import json
from pathlib import Path

from sigma_match import rule_matches

ROOT = Path(__file__).resolve().parent.parent
RULE = ROOT / "detections/sigma/http_odd_ua.yml"
SAMPLES = ROOT / "tests/samples"


def load(name):
    lines = (SAMPLES / name).read_text().splitlines()
    return [json.loads(line) for line in lines if line.strip()]


def test_rule_fires_on_python_requests_ua():
    assert all(rule_matches(RULE, ev) for ev in load("ecs_http_ua_positive.json"))


def test_rule_stays_quiet_on_browser_ua():
    assert not any(rule_matches(RULE, ev) for ev in load("ecs_http_ua_negative.json"))
