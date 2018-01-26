Feature: Customer search
  Verify if a customer exists in customer's list

  Scenario: Search for a customer
    Given I enter Franco as name of the client
    When I search for the customer
    Then The customer should be present in the customer's list