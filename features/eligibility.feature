Feature: Housing register eligibility check
  As a resident of the borough
  I want to check whether I am eligible to join the housing register
  So that I know whether to submit a full housing application

  Scenario: A resident who meets both rules is eligible
    Given the resident enters an age of "30"
    And the resident enters "5" years lived in the borough
    When the resident checks their eligibility
    Then the result should be "Eligible"

  Scenario Outline: Eligibility at the age and residency limits
    Given the resident enters an age of "<age>"
    And the resident enters "<years>" years lived in the borough
    When the resident checks their eligibility
    Then the result should be "<result>"

    Examples:
      | age | years | result                                                                |
      | 17  | 5     | Not eligible: you must be 18 or over                                  |
      | 18  | 2     | Eligible                                                              |
      | 30  | 1     | Not eligible: you must have lived in the borough for at least 2 years |

  Scenario Outline: Invalid details are rejected without a decision
    Given the resident enters an age of "<age>"
    And the resident enters "<years>" years lived in the borough
    When the resident checks their eligibility
    Then the resident should see the error "<error>"

    Examples:
      | age | years | error                                                    |
      | abc | 5     | Age must be a whole number of 0 or more                  |
      | -1  | 5     | Age must be a whole number of 0 or more                  |
      | 30  | two   | Years in the borough must be a whole number of 0 or more |
