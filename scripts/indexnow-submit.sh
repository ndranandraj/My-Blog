#!/usr/bin/env bash
# Ping IndexNow-capable search engines (Bing, Yandex, DuckDuckGo, Seznam) with
# a list of URLs that need re-crawling. Google doesn't participate in IndexNow
# directly — for that use Search Console's "Request Indexing" or rely on
# sitemap pings.
#
# Usage:
#   ./scripts/indexnow-submit.sh \
#     https://ndranandraj.com/posts/tn-2026-dummy-candidates/ \
#     https://ndranandraj.com/data/tn-2026-candidates/
#
# With no args it submits just the homepage.
#
# Key is read from hugo.toml. If you rotate the key:
#   1. openssl rand -hex 16 > /tmp/new.key
#   2. Update params.indexNow.key in hugo.toml to the new value
#   3. Rename static/OLD.txt to static/NEW.txt and update its contents
#   4. Commit + deploy
#
set -euo pipefail

HOST="ndranandraj.com"
KEY="9c9bdc14f5d62a6f18f1c69a5ff43a6a"
KEY_LOCATION="https://${HOST}/${KEY}.txt"

URLS=("$@")
if [[ ${#URLS[@]} -eq 0 ]]; then
  URLS=("https://${HOST}/")
fi

# Build the urlList JSON array
URL_LIST_JSON=$(printf '"%s",' "${URLS[@]}")
URL_LIST_JSON="[${URL_LIST_JSON%,}]"

PAYLOAD=$(cat <<EOF
{
  "host": "${HOST}",
  "key": "${KEY}",
  "keyLocation": "${KEY_LOCATION}",
  "urlList": ${URL_LIST_JSON}
}
EOF
)

echo "→ Submitting ${#URLS[@]} URL(s) to IndexNow"
for u in "${URLS[@]}"; do echo "    $u"; done
echo ""

# Submit to Bing's IndexNow endpoint (syndicates to Yandex, DuckDuckGo, Seznam)
echo "→ POST https://api.indexnow.org/indexnow"
RESPONSE=$(curl -sS -w "\n%{http_code}" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "$PAYLOAD" \
  https://api.indexnow.org/indexnow)

BODY=$(echo "$RESPONSE" | sed '$d')
CODE=$(echo "$RESPONSE" | tail -n1)

echo "  Response: HTTP $CODE"
if [[ -n "$BODY" ]]; then echo "  Body: $BODY"; fi

case "$CODE" in
  200|202) echo "✓ Accepted" ;;
  400)     echo "✗ Bad request — check payload" ;;
  403)     echo "✗ Key verification failed — is $KEY_LOCATION serving the key?" ;;
  422)     echo "✗ URLs don't match host or key mismatch" ;;
  429)     echo "✗ Too many requests — back off" ;;
  *)       echo "? Unexpected response" ;;
esac
