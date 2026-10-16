# Template da copiare al bisogno

## Task

```markdown
# Nome task
## Problema
## Acceptance
- [ ] Comportamento osservabile richiesto
## Scope
File o aree coinvolte; esclusioni concordate
## Depends on
Nessuna / task prerequisiti
## Verification
Comandi reali del progetto e osservazioni necessarie
```

## progress/current/<task>.md

```markdown
# Nome task
Task source:
Branch/worktree:
## Plan
## Baseline
## Log
## Blockers
## Next step
Un'azione concreta per riprendere il lavoro.
```

## progress/impl/<task>.md

```markdown
# Implementation
## What changed and why
## Verification
Comando → exit code → osservazione; controlli saltati espliciti.
## Deliberately skipped
## Open questions
```

## progress/review/<task>.md

```markdown
# Review
Verdict: APPROVED | CHANGES_REQUESTED
## Acceptance evidence
## Diff reviewed
Base di confronto e stato delle modifiche esaminate.
## Checks run
## Required changes
## Limitations
```

## progress/history/<task>.md

```markdown
# Completed session
## Result
## Verification and review
## Deliberately skipped
## Follow-up
```
