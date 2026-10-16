# Project instructions

## Project context — fill in before using

- Product and users: TO CONFIGURE
- Stack: TO CONFIGURE
- Important directories: TO CONFIGURE
- Architecture constraints: TO CONFIGURE
- Existing verification commands: TO CONFIGURE
- Integration environment and safe local data: TO CONFIGURE

Do not invent missing commands or treat these placeholders as completed setup.

## Working rules

1. Read the task, relevant code and callers before editing. Fix the root cause.
2. Prefer existing helpers, standard libraries and native platform features.
3. Use the smallest change that meets the agreed acceptance criteria.
4. Preserve input validation, security, error handling and accessibility.
5. Record pre-existing failures before changing code. Never describe skipped or
   unavailable checks as passed.
6. Verify meaningful logic with a runnable check in the existing test runner.
   For UI and integration work, record what you actually observed.
7. For work spanning sessions, keep a per-task progress file using
   harness/TEMPLATES.md. Record the next concrete action while working.
8. Review the actual diff against the acceptance criteria. A report is not proof.
9. Keep unrelated user changes. Do not copy secrets into reports or commits.
10. External actions require authorization consistent with the user's request.

## Parallel work, when explicitly requested

Use one feature per worktree. Isolate ports and databases where applicable.
Assign complete producer/consumer contracts, not arbitrary chunks of files.
Do not let two agents edit the same scope without coordination.

## Source of truth

This file owns project rules. Role prompts refine responsibilities; they must
not duplicate stack details. Historical progress describes past work, not
current instructions. Flag conflicts instead of silently following stale notes.
