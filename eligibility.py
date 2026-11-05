"""Housing register eligibility checker."""

MINIMUM_AGE = 18
MINIMUM_YEARS_IN_BOROUGH = 2


def check_eligibility(age_text, years_text):
    """Return the eligibility result for the details a resident enters.

    Raises ValueError with a message for the resident if a detail is invalid.
    """
    age = to_whole_number(age_text, "Age")
    years_in_borough = to_whole_number(years_text, "Years in the borough")

    if years_in_borough > age:
        raise ValueError("Years in the borough cannot be more than age")

    if age < MINIMUM_AGE:
        return f"Not eligible: you must be {MINIMUM_AGE} or over"
    if years_in_borough < MINIMUM_YEARS_IN_BOROUGH:
        return f"Not eligible: you must have lived in the borough for at least {MINIMUM_YEARS_IN_BOROUGH} years"
    return "Eligible"


def to_whole_number(text, field_name):
    """Convert text to a whole number of 0 or more, or raise ValueError."""
    text = text.strip()
    if not text.isdecimal():
        raise ValueError(f"{field_name} must be a whole number of 0 or more")
    return int(text)