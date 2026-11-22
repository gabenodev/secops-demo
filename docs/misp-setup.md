# MISP setup notes (R-04)

Fill this in after you bring up [misp-docker](https://github.com/MISP/misp-docker) next to this repository.

## Date

- Setup date:

## Ports

- `NGINX_HTTP_PORT=8081`
- `NGINX_HTTPS_PORT=8444`
- `BASE_URL=https://localhost:8444`

## Image digests actually pulled

```
# paste: docker images --digests | grep misp
```

## Feed

- Feed name: CIRCL OSINT Feed
- Fetch date:
- Events present with `to_ids` attributes: yes / no
