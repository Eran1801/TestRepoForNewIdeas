# AI-Driven Feature Spec → Jira Pipeline

Personal reference notes on the pipeline I built at InManage: turns a raw feature spec into
a tracked, developer-ready Jira ticket with minimal manual typing, then hands off to QA
automatically once dev is done. ~50 specs run through this so far.

## Why

Before this, feature specs came in ad hoc (Slack message, doc, verbal handoff), someone
manually wrote the Jira ticket, summaries were inconsistent, and QA found out a ticket was
"ready" whenever a dev happened to mention it. Bottleneck was all the manual glue work.

## Pipeline stages

```
1. Spec intake        -> raw feature spec (doc/Slack/notes)
2. Jira ticket creation -> structured ticket, correct project/type/fields
3. AI task summary     -> agent drafts a dev-facing task breakdown on the ticket
4. Developer execution -> dev picks it up, works it, transitions status
5. QA handoff          -> automated, triggered off status transition
```

### 1. Spec intake

Input is whatever form the feature request shows up in — a doc, a Slack thread, a paragraph
from a PM. No fixed template required; the agent reading it just needs:
- what the feature/change is
- why (context/motivation)
- any known constraints (API, data model, deadline)

If the spec is too thin to act on, the agent should ask clarifying questions before creating
a ticket — better to stop here than to create a vague ticket downstream.

### 2. Jira ticket creation

Done via Atlassian MCP tools (`createJiraIssue`, or `getJiraIssueTypeMetaWithFields` /
`getJiraProjectIssueTypesMetadata` first if the project's required fields aren't known yet).

Minimum fields set on creation:
- **Project** + **Issue type** (Story/Task/Bug — inferred from the spec, default to Task if
  ambiguous)
- **Summary** — short, action-oriented (e.g. "Add retry logic to payment webhook handler")
- **Description** — the original spec content, lightly cleaned up, not paraphrased away
- **Labels/Components** — if the project uses them for routing (e.g. `backend`, `ai-pipeline`)

Skip inventing values for custom fields you don't have data for — leave them for the dev or
PM rather than guessing.

### 3. AI-agent-drafted task summary

Once the ticket exists, the agent adds a comment (`addCommentToJiraIssue`) with a dev-facing
breakdown:
- Scope: what's actually in/out for this ticket
- Suggested approach / files or services likely touched
- Open questions or risks worth flagging before someone starts

This is a starting point for the developer, not a spec they're locked into — the point is
cutting the "where do I even start" time, not prescribing the implementation.

### 4. Developer execution

Normal dev flow: pick up ticket, do the work, transition status as they go
(`transitionJiraIssue`, checking valid transitions first with `getTransitionsForJiraIssue`).
The one convention that matters for the pipeline: **the status transition to "Ready for QA"
(or equivalent) is the trigger for stage 5** — so it has to actually be used, not skipped by
closing straight to Done.

### 5. Automated QA handoff

Triggered off the status transition in step 4. At minimum:
- Comment added to the ticket summarizing what changed (can pull from the PR/commit if linked)
- QA-relevant info surfaced: what to test, what changed, any manual test steps called out by
  the dev
- Ticket assigned/routed to QA queue

This is the piece that closes the loop — before this existed, "is this ready for QA" was a
manual check-in.

## Stack notes

- **Claude Code**: hooks + slash commands + skills to run each stage without a bespoke app
- **MCP**: Atlassian MCP server for all Jira read/write (no direct REST calls needed)
- **Where custom logic lived**: AWS Lambda (Python/FastAPI) for anything that needed to run
  outside an interactive agent session — e.g. reacting to a Jira webhook for the QA handoff
  trigger, since that has to fire even if no one's actively driving an agent session at that
  moment

## Things that mattered in practice

- **Don't skip the clarifying-question step.** A ticket created from a vague spec just moves
  the ambiguity downstream to the dev, which is worse than catching it at intake.
- **Keep the AI summary advisory, not authoritative.** Early version had devs treating the
  drafted breakdown as gospel; had to explicitly frame it as a starting point.
- **The QA trigger has to be a real status transition**, not a convention people forget.
  Automating off an event beats relying on someone remembering to ping QA.
- **Idempotency on ticket creation** — same spec shouldn't create duplicate tickets if the
  pipeline runs twice (e.g. retried after a transient MCP/API failure). Check for an existing
  ticket with the same source spec reference before creating a new one.
