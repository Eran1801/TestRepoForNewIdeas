# CONTEXT

Shared language for this project. Written so an agent picking up work here uses one word per concept instead of five.

Built using the `domain-modeling` skill from [mattpocock/skills](https://github.com/mattpocock/skills).

## The name collision to know about first

The word **"spec"** means two different things in this project, and we used it for both for most of this project's history. They are now separated:

| Term | Means | Never call it |
|---|---|---|
| **אפיון** (*ifyun*) | The **input**: a Hebrew PowerPoint functional-specification deck, written by a product person, that our system reads. | "the spec" |
| **product spec** (`spec.md`) | The **output of our own planning**: the document describing the system *we* are building. | "the אפיון" |

The system reads an **אפיון**. The system is described by the **product spec**. If a sentence is ambiguous about which one it means, it is wrong.

## Glossary

**אפיון** — a PowerPoint (`.pptx`) functional spec, always Hebrew, written by a product person. The system's only input document. Converted to Markdown by `markitdown` before anything reads it.

**שקופית** (slide) — one slide of the אפיון. The unit of traceability: every משימה records the שקופית it came from, and the UI links the two.

**דרישה** (requirement) — one statement inside the אפיון that implies work. A single שקופית usually holds several. Requirements are what the analysis engine extracts; they are not yet משימות.

**משימה** (task) — one Jira issue of type `Task`, derived from a דרישה. Always type `Task` — never Story, Bug, or Epic. This is the domain object.

**קוביה** (card) — the **UI representation** of a משימה on the board, before and after creation. A קוביה is not a separate thing from a משימה; it is how one is displayed. Say "משימה" when talking about the work, "קוביה" only when talking about the screen.

**הצלבה** (cross-reference) — matching an אפיון against the existing source code to determine what is already built. The step that distinguishes this product from a plain summarizer.

**כבר קיים בקוד** (already-in-code) — a דרישה the הצלבה found already implemented. Renders de-emphasized, is excluded from "create all", and carries the file path and line where it was found. It is *not* deleted — the PM must be able to see it and disagree.

**ציטוט** (quote) — the verbatim sentence from the אפיון that produced a משימה. Always shown, never optional. Its purpose is to let a project manager audit the system's reading without opening the PowerPoint.

**היקף** (scope) — whether a משימה is server-side or client-side. Exactly one of the two; never "both". A דרישה touching both sides becomes **two independent משימות** (see ADR-001).

**Board** — the Jira board, identified by a URL the user supplies. The source of truth for the available Epics, users, and statuses. The system never invents these values.

## Decisions

### ADR-001: a requirement touching both sides becomes two independent Tasks

**Status:** accepted.

A דרישה that needs both server and client work is split into two sibling משימות, each a top-level `Task` with its own Jira key, status, assignee, and history. It is *not* one parent Task with two Sub-tasks.

**Why:** the two sides are usually picked up by different developers, on different schedules. A parent/sub-task shape couples them: closing the parent implies both are done, and the sub-task inherits the parent's position in the backlog. Two siblings can be scheduled, assigned, and closed independently.

**Known tension:** this produces a *horizontal* slice (one layer per ticket), which the `to-tickets` skill argues against in favour of vertical tracer bullets that are demoable alone. We accept the trade: see "Open questions" below.

**Sub-tasks still exist** for a different purpose — breaking one large single-side משימה into stages. That is unrelated to the server/client split.

### ADR-002: Jira is reached over REST, not MCP

**Status:** accepted.

The system talks to Jira through the Jira REST API v3 from its own backend. MCP is not used.

**Why:** MCP connects an interactive LLM agent to tools inside a session. Our system is a long-lived application: a user clicking "צור" needs a fast, deterministic HTTP call, not a round-trip through a model. MCP would also have no session to live in when the backend runs unattended.

**Auth:** an API token is enough for a single internal organisation; OAuth 2.0 (3LO) is required if each user connects their own Jira account.

### ADR-003: `markitdown` runs as Python regardless of backend language

**Status:** accepted.

`markitdown` is a Python-only Microsoft library. If the main backend is PHP, the conversion step runs as a separate Python process or service rather than being reimplemented in PHP.

**Why:** reimplementing PPTX parsing loses the thing we chose the library for. The boundary is cheap — one file in, one Markdown file out.

## Open questions

Not yet settled; resolve with `grill-with-docs` before the relevant tickets start.

1. **Vertical vs horizontal slicing.** ADR-001 makes tickets horizontal by design. Does the team want a demoable-alone tracer bullet instead (one משימה per דרישה, with server and client work inside it), accepting that two people then share a ticket? The current answer is no, but it was decided before the tracer-bullet argument was on the table.
2. **How the הצלבה actually decides "already built".** Today this is asserted, not implemented. Is it embedding search over the repo, a symbol index, an LLM pass over candidate files, or a human-confirmed suggestion? This is the product's core claim and its hardest engineering problem.
3. **Idempotency key.** Re-running the same אפיון must not create duplicate משימות. What identifies a משימה across runs — a hash of the ציטוט, the שקופית number plus title, or a marker written back into the Jira issue?
4. **Who owns the אפיון→משימה mapping after creation?** If the אפיון is edited and re-run, do existing Jira issues get updated, or is a new run always additive?
