Feature: Validate of inputs
  Validate inputs using regular expressions

  Scenario: Validate user data
    Given I enter 03123 as zip code
      And I enter Bolivia_ as country
      And I enter 300,000,000 as quantity of habitants