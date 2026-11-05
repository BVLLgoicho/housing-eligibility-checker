"""Housing register eligibility checker."""

MINIMUM_AGE = 18
MINIMUM_YEARS_IN_BOROUGH = 2


def check_eligibility(age_text, years_text):
    """Return the eligibility result for the details a resident enters."""
    age = int(age_text)
    years_in_borough = int(years_text)

    if age < MINIMUM_AGE:
        return "Not eligible: you must be 18 or over"
    if years_in_borough < MINIMUM_YEARS_IN_BOROUGH:
        return "Not eligible: you must have lived in the borough for at least 2 years"
    return "Eligible"
