# Open questions

Each entry is marked `blocking` or `non_blocking`.

## Q-001 (non_blocking): regulation sources unreachable
Official hosts for all four regimes (ecfr.gov, ftc.gov, federalregister.gov, govinfo.gov, ico.org.uk, eur-lex.europa.eu, gov.il, nevo.co.il, knesset.gov.il) are blocked by the environment's egress policy. Operator chose to allowlist them but cannot do so from the iPhone app; it must be done at claude.ai/code on desktop. Until then, `all:regulation` tasks are moved to the end of the queue and academic cells proceed via the PMC Open Access dataset (tools/pmc_fetch.sh). Unofficial GitHub mirrors are NOT used (primary-source rule).
