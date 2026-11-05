"""Unit tests for the eligibility rules and input validation (pytest)."""
import pytest

from eligibility import check_eligibility, to_whole_number


def test_whole_number_text_is_converted():
    assert to_whole_number("18", "Age") == 18


def test_surrounding_spaces_are_ignored():
    assert to_whole_number(" 5 ", "Age") == 5


@pytest.mark.parametrize("bad_text", ["abc", "-1", "17.5", ""])
def test_invalid_text_is_rejected(bad_text):
    with pytest.raises(ValueError, match="Age must be a whole number of 0 or more"):
        to_whole_number(bad_text, "Age")


def test_years_in_borough_greater_than_age_is_rejected():
    with pytest.raises(ValueError, match="Years in the borough cannot be more than age"):
        check_eligibility("30", "40")


def test_years_in_borough_equal_to_age_is_allowed():
    assert check_eligibility("30", "30") == "Eligible"
