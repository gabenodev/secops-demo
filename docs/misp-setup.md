# MISP setup notes (R-04)

Fill this in after you bring up [misp-docker](https://github.com/MISP/misp-docker) next to this repository.

## Date

- Setup date: 2026-11-22

## Ports

- `NGINX_HTTP_PORT=8081`
- `NGINX_HTTPS_PORT=8444`
- `BASE_URL=https://localhost:8444`

## Image digests actually pulled

```
ghcr.io/misp/misp-docker/misp-modules  latest  sha256:08d4cf35861fe2ee753023a207bb5380506f078750559620ae7f9736e186dea3
ghcr.io/misp/misp-docker/misp-core     latest  sha256:33627106f4962082fd7c58ac0cd15576c55c8ae672ca311699fe652e59c432dc
ghcr.io/misp/misp-docker/misp-nginx    latest  sha256:4c1c78e634b56e96e8a801f6e325642faaa5ae236fe71f97fad0831148c796f3
```

## Feed

- Feed name: CIRCL OSINT Feed
- Fetch date: 2026-11-22
- Events present with `to_ids` attributes: yes (14 events after fetch)
