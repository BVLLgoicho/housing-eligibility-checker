# Housing Register Eligibility Checker

A small Python prototype for a local authority's resident-facing services.
It tells a resident whether they can join the council's housing register,
and why. Its expected behaviour is written as Behaviour-Driven Development
(BDD) scenarios in Gherkin and run with `behave`.

Module: SWE6301 Agile Programming, Assignment 1 (Task 2)

## Stakeholders

- **Main user:** a resident of the borough who wants to apply for social housing.
- **Service manager:** the housing officer who owns the eligibility rules.
- **Developers:** the team who build and maintain the service.

## Problem

Residents often submit full housing applications without knowing whether
they meet the basic rules. Ineligible applications waste residents' time
and take up housing officers' time to process and reject. A quick, clear
eligibility check before applying avoids this.

## User story

> As a resident of the borough,
> I want to check whether I am eligible to join the housing register,
> so that I know whether to submit a full housing application.

## Eligibility rules (simplified for this prototype)

1. The applicant must be **18 or over**.
2. The applicant must have lived in the borough for **at least 2 years**.

## Acceptance criteria

1. A resident aged 18 or over who has lived in the borough for 2 or more
   years is told they are **eligible**.
2. A resident under 18 is told they are **not eligible**, with the reason.
3. A resident who has lived in the borough for less than 2 years is told
   they are **not eligible**, with the reason.
4. A resident who is exactly 18 and has lived in the borough for exactly
   2 years is **eligible** (boundary).
5. If the age or years lived in the borough is not a whole number of zero
   or more, the resident sees an error message and no decision is made.

## Project files

- `features/eligibility.feature`: the BDD scenarios (Gherkin)
- `features/steps/eligibility_steps.py`: step definitions linking scenarios to code
- `eligibility.py`: the eligibility rules and input validation
- `evidence/`: saved `behave` output from each stage (red, partly green, green)

## How to run

Requires Python 3 and behave:

```
pip install behave
behave
```
