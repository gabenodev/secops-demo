# Front door from Lab 3: nginx terminates TLS in front of OpenSearch Dashboards.
# Pinned by tag and digest, so the build never floats (Lab 3 check list).
FROM nginx:1.29-alpine@sha256:5616878291a2eed594aee8db4dade5878cf7edcb475e59193904b198d9b830de

# Site config only. Certificates stay out of the image and are mounted at runtime
# from certs/ (git-ignored), exactly as in compose.yaml.
COPY frontdoor.conf /etc/nginx/conf.d/default.conf

EXPOSE 443
