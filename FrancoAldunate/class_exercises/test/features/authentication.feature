Feature: Authenticate
  Login in to the application

  Scenario: Successful login with PIN
    Given I have pushed my card in the slot 1
    When I enter my PIN
      And I press "OK"
    Then I should see the main menu
