# Research log

#0 | n/a | bootstrap | ok | created research/, 28 cells, 59 queued tasks (regulation collect split per regime), max_iterations 80, scope auto
#1 | offline (WebSearch works; WebFetch and curl blocked by egress proxy for ecfr.gov, ftc.gov, federalregister.gov, ecfr.io, eur-lex.europa.eu, pubmed) | T-0005 grade all:regulation | needs_sources | corpus empty; T-0001..T-0004 collect tasks left in queue; no sources saved (rule 5: search snippets are not retrieved text)
#1a | probe | network routes | ok | egress blocks gov/EU/academic hosts; WORKS: WebSearch (discovery), raw.githubusercontent.com, S3 incl. NCBI PMC Open Access dataset (verbatim full text, see tools/pmc_fetch.sh), Google Drive connector. Regulation primary texts still unreachable.
#1b | operator | queue reorder | ok | regulation tasks moved to end of queue pending domain allowlist (Q-001); academic cells proceed via PMC OA on S3
#2 | online (search) + PMC OA S3 fetch | T-0006 collect 4-6:parent_trust | 7 saved (S-0001..S-0007) | 4 queries (parent app selection; parental mediation review; manipulative design/ads content analysis; parent concerns preschool tablets). Saved all full text. Skipped PMC9645666 (theory paper, no empirical type). Not attempted: PubMed-only hits (no OA full text), arxiv (blocked). Added tools/save_pmc.py (verbatim body, refs dropped; verified substring match).
