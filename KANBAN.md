# Kanban Board

The live board is on GitHub:
[Housing Eligibility Checker - Kanban](https://github.com/users/BVLLgoicho/projects/4).
Each card is a GitHub issue, and commits close their card with `Closes #n`.

## Columns and policies

| Column | Colour | Policy |
|---|---|---|
| Backlog | Grey | Ordered list of work not started yet |
| In Progress (WIP 1) | Red | Only 1 card at a time ("stop starting, start finishing"). A failing test is written first |
| Testing | Amber | Code is written; `pytest` and `behave` are run |
| Done | Green | Meets the Definition of Done in the README |

A new card is pulled into *In Progress* only when the WIP limit allows.

The board was introduced after the first working version (commit `f13217d`);
cards #1 to #5 for the earlier work were added to *Done* afterwards as a record.

## Final state

| Card | Work | Commit(s) |
|---|---|---|
| #1 | User story and acceptance criteria | `95cbd45` |
| #2 | BDD scenarios written before code | `ae22d60` |
| #3 | Eligibility rules and step definitions | `6f9adb1` |
| #4 | Input validation for invalid details | `38f9ffd` |
| #5 | Definition of Done and Kanban board | `f13217d`, `4c6dfb3` |
| #10 | Reject years in the borough greater than age | `96ada8b`, `7a63232`, `661d599` |
| #11 | Refactor result messages to use rule constants (Boy Scout Rule) | `0706aa6` |
| #8 | Update README with pytest instructions | this commit |
