# secops-demo

Self-hosted security telemetry stack: OpenSearch, Logstash, Sigma detections, MISP enrichment and a TLS nginx front door.

Built from Labs 3–6. Every change cites a risk ID in `RISK-REGISTER.md`.

## Stack

| Service | Role |
|---------|------|
| OpenSearch 2.19.1 | Search and store Suricata events |
| OpenSearch Dashboards | Discover and rule queries |
| Logstash (OSS + OpenSearch output) | Normalise Suricata EVE to ECS, enrich with IoCs |
| nginx front door | TLS termination for Dashboards |

Images are pinned by digest in `.env`. Secrets live only as SOPS ciphertext under `secrets/`.

## Commands

```bash
cp .env.example .env
make secrets   # decrypts into .env.secrets (git-ignored)
make up
make test
make down
```

On Windows without GNU Make, run the same steps with Docker Compose and sops directly (see `docs/README.md`).

## What you still do locally

1. Start Docker Desktop.
2. Keep `SOPS_AGE_KEY_FILE` pointed at your age private key (`~/.config/sops/age/keys.txt`).
3. Issue lab certificates with step-ca into `certs/` (Lab 3 Part C) before the front door will serve HTTPS.
4. For Lab 6: run MISP beside this repo, then `sops edit secrets/intel.enc.yaml` with your MISP and Shodan keys.

Admin password ciphertext is already in `secrets/opensearch.enc.yaml` for the age recipient in `.sops.yaml`. If you regenerate the age key, re-encrypt that file.
