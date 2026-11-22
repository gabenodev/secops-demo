# secops-demo docs

Self-hosted security telemetry: OpenSearch, Logstash, Sigma detections and MISP enrichment.

## Risks closed here

| ID | Control in this repo |
|----|----------------------|
| R-01 | PR-only `main`, governance workflow, pre-commit branch guard |
| R-02 | SOPS/age secrets, gitleaks, digests in `.env` |
| R-03 | Sigma + pipeline pytest (positive and negative samples) |
| R-04 | MISP pull into Logstash `translate`, tagged and scored |
| R-05 | Shodan snapshot script and `monitoring/alerts.yml` |

## Quick start

1. Copy `.env.example` to `.env`.
2. Install `sops` and `age`, put your age private key in `~/.config/sops/age/keys.txt`, and set `SOPS_AGE_KEY_FILE`.
3. Decrypt with `make secrets` (creates `.env.secrets`, git-ignored).
4. Issue `certs/frontdoor.crt` and `certs/frontdoor.key` with step-ca (Lab 3 Part C).
5. Seed `enrich/ioc_ip.yml` (empty dict is fine until MISP runs): `mkdir -p enrich && echo '{}' > enrich/ioc_ip.yml`
6. `make up`, then poll OpenSearch health until green.

Evidence screenshots and health outputs go under `docs/evidence/`.
