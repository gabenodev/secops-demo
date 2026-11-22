# Front door from Lab 3: nginx terminates TLS in front of OpenSearch Dashboards.
# Pinned by tag and digest, so the build never floats (Lab 3 check list).
FROM nginx:1.27-alpine@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10

# Site config only. Certificates stay out of the image and are mounted at runtime
# from certs/ (git-ignored), exactly as in compose.yaml.
COPY frontdoor.conf /etc/nginx/conf.d/default.conf

EXPOSE 443
