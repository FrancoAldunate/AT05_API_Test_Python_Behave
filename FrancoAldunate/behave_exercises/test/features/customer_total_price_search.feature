Feature: Customer total price search
  Validate successful searching of customer total price

  Scenario Outline: Search a customer total price with valid data
    Given I enter <name> as name of the client
      And I enter <id> as id of the client
      And I enter <total-price> as the total price of purchase
    When I search for the customer total price
    Then The total price should be found in the customer's total price list

    Examples:

      | name      | id | total-price |
      | Franco    | 1  | 500         |
      | Raul      | 2  | 700         |
      | Daniel    | 3  | 70          |
      | Alejandra | 4  | 800         |
      | Daniela   | 5  | 1200        |