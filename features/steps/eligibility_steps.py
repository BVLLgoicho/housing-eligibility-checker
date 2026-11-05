from behave import given, when, then

from eligibility import check_eligibility


@given('the resident enters an age of "{age}"')
def step_enter_age(context, age):
    context.age = age


@given('the resident enters "{years}" years lived in the borough')
def step_enter_years(context, years):
    context.years = years


@when("the resident checks their eligibility")
def step_check_eligibility(context):
    try:
        context.result = check_eligibility(context.age, context.years)
        context.error = None
    except ValueError as error:
        context.result = None
        context.error = str(error)


@then('the result should be "{expected}"')
def step_result_should_be(context, expected):
    assert context.result == expected, f"Expected {expected!r} but got {context.result!r}"


@then('the resident should see the error "{expected}"')
def step_error_should_be(context, expected):
    assert context.error == expected, f"Expected error {expected!r} but got {context.error!r}"
