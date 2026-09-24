#!/usr/bin/env bash
# Fetch verbatim full text of a PubMed Central open-access article from the
# NCBI PMC Open Access dataset on AWS (pmc-oa-opendata), the one route to
# journal full text that the session's egress policy allows.
# Usage: tools/pmc_fetch.sh PMC9209675 [out_file]
set -euo pipefail
id="$1"; out="${2:-/dev/stdout}"
bucket="https://pmc-oa-opendata.s3.amazonaws.com"
key=$(curl -sS -m 30 "$bucket/?list-type=2&prefix=${id}." | grep -o "<Key>[^<]*\.txt</Key>" | sed 's/<[^>]*>//g' | tail -1)
[ -z "$key" ] && { echo "not in PMC OA dataset: $id" >&2; exit 1; }
curl -sS -m 60 "$bucket/$key" -o "$out"
