# Contributing to Tactical Mobile Game

We welcome contributions from the team! To keep our codebase clean, optimized, and stable, please follow these guidelines when adding features or fixing bugs.

---

## Branching Workflow

1. **Create a Feature Branch**: Never push directly to `main`. Create a descriptive branch for your task:
   * `feature/ballistics-update`
   * `bugfix/touch-controls`
   * `net/multiplayer-sync`
2. **Keep Branches Updated**: Regularly pull changes from `main` into your working branch to avoid merge conflicts.

---

## Coding Standards

* **Python & C#**: Follow clean coding practices, include comments for complex math or simulation loops, and ensure all unit tests pass before submitting.
* **Testing**: Add or update unit tests in the `tests/` directory for any new logic you introduce.

---

## Pull Request Process

1. Open a Pull Request (PR) against the `main` branch.
2. Ensure all automated GitHub Actions CI tests pass successfully.
3. Request a review from a team member before merging your code.
