---
name: finish-iteration
description: Runs verification tests, checks for repository litter, and updates AGENTS.md state before Git commit.
---

# Finish Iteration Checklist
1. Check `git status` and remove any temporary/scratch files outside `artifacts/`.
2. Execute `pytest` to confirm all physical sanity checks pass on `data/sample/`.
3. Update the `Current State` section in `AGENTS.md` with what was built and the exact CLI command to reproduce the results.
4. Provide a clean, conventional commit message (e.g., `feat(iter-1): implement OpenCV track rectification and metal line extraction`).
