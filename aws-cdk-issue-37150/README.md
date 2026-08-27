# aws/aws-cdk#37150 — StateMachine `timeout` silently ignored for `.asl.json` definitions

Issue: https://github.com/aws/aws-cdk/issues/37150

## What we scanned

Searched `aws/aws-cdk` for open, unclaimed, "good first issue"/`effort/small`-`effort/medium`
bugs. Most well-scoped candidates already had an open PR against them within days of being
filed (the backlog moves fast). This one — filed 2026-03-03, 1 comment, no assignee, no linked
PR at the time of scanning — was the cleanest unclaimed match.

## Root cause

`StateMachineProps.timeout` is only ever applied when the state machine's `definitionBody` is
a `ChainDefinitionBody` (i.e. built from `DefinitionBody.fromChainable()` / the deprecated
`definition` prop). In `packages/aws-cdk-lib/aws-stepfunctions/lib/state-machine.ts`:

```ts
let graph: StateGraph | undefined = undefined;
if (definitionBody instanceof ChainDefinitionBody) {
  graph = new StateGraph(definitionBody.chainable.startState, 'State Machine definition');
  graph.timeout = props.timeout;   // <-- only path that ever reads props.timeout
  ...
}
```

`graph.timeout` gets serialized as the top-level `TimeoutSeconds` key when the chain is
rendered to ASL JSON (`state-graph.ts`). But `FileDefinitionBody` (`DefinitionBody.fromFile()`,
e.g. a `.asl.json` file) and `StringDefinitionBody` (`DefinitionBody.fromString()`) have their
own `bind()` implementations that never look at `props.timeout` at all — and `DefinitionConfig`
(their return type) has no `timeoutSeconds` field to plumb it through even if they wanted to.
So `timeout` is silently dropped whenever the definition isn't built as a chain — exactly the
"unexpected behavior" the issue reports.

## Fix

Two behaviors were considered:
1. Parse the file/string definition JSON at synth time and merge in `TimeoutSeconds`.
2. Fail fast with a clear error telling the user where `TimeoutSeconds` actually belongs.

Went with (2): `FileDefinitionBody` content lives in an S3 asset CDK never parses (parsing it
to inject a field risks corrupting non-JSON or token-bearing content and complicates asset
staging), and `StringDefinitionBody` may already set `TimeoutSeconds` itself, making silent
merging ambiguous. This is also the existing convention in this file for unsupported prop
combinations (see `ConflictingDefinitionProperties` / `MissingDefinition` a few lines up).

Changes (`fix.patch`):
- `state-machine.ts`: throw a `ValidationError` when `timeout` is set together with a
  non-chainable `definitionBody`, naming `TimeoutSeconds` as the field to set directly in the
  ASL definition. Updated the `timeout` prop's JSDoc to state the limitation up front.
- `state-machine.test.ts`: added a test that the new error fires for `fromString()`, and a
  regression test that `timeout` still renders into `TimeoutSeconds` for the chainable path.

Confirmed (via repo-wide grep) that no existing test or integ test in the repo combines
`timeout` with `fromFile()`/`fromString()`, so this doesn't newly break anything that
previously relied on the silent drop.

## Validation

Ran in a full local clone + build of `aws-cdk-lib` (`npx lerna run build --scope=aws-cdk-lib`,
per CONTRIBUTING.md):

- `npx jest aws-stepfunctions/test/state-machine.test.ts` → **42/42 passed** (incl. the 2 new tests)
- `npx jest aws-stepfunctions/test/` → **375/375 passed**, 22/22 suites (no regressions elsewhere in the module)
- `npx eslint aws-stepfunctions/lib/state-machine.ts aws-stepfunctions/test/state-machine.test.ts` → clean

## Why this lives here instead of a PR

This session is scoped to `eran1801/testrepofornewideas`; it can read `aws/aws-cdk` publicly
but isn't attached with push credentials there (attaching a second repo from a different owner
isn't supported in the same session). `fix.patch` is the real, tested diff — to actually open
the PR:

```
gh repo fork aws/aws-cdk --clone=false   # or fork via the GitHub UI
git clone <your fork> && cd aws-cdk
git checkout -b fix/37150-statemachine-timeout-validation
git apply /path/to/fix.patch
git commit -am "fix(stepfunctions): validate timeout is unsupported with file/string definitionBody"
git push -u origin fix/37150-statemachine-timeout-validation
gh pr create --repo aws/aws-cdk --title "fix(stepfunctions): timeout with file/string definitionBody" --body "Closes #37150"
```

Or say the word and a fresh session scoped to `aws/aws-cdk` (with push access) can fork, push,
and open the PR directly.
