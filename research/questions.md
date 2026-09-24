# Open questions

Each item is marked `blocking` or `non_blocking`.

## Q-001 | blocking | Network access denies every research source

Raised in iteration #1 while working `all:regulation`.

The environment's egress policy denied every source host tried: www.ecfr.gov, www.ftc.gov, ico.org.uk, eur-lex.europa.eu, gdpr-info.eu, www.legislation.gov.uk, www.gov.il, pmc.ncbi.nlm.nih.gov, pubmed.ncbi.nlm.nih.gov, www.apa.org, publications.aap.org, www.unicef.org, doi.org, www.frontiersin.org, en.wikipedia.org. Web search returns titles and snippets only, and rule 5 forbids citing a source that was not opened. No findings can be recorded.

Decision needed: widen the environment's network access (or allow these hosts, plus academic publishers), then restart the loop. Iteration #1 was not counted as a failed attempt on `all:regulation`, and `dry_streak` was not incremented, because the failure is environmental, not a lack of evidence.
