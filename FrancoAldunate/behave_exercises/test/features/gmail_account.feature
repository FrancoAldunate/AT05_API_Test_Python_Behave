Feature: Gmail account
  Validate creation of Gmail account

  Scenario: Validate user data
    Given I go to www.google.com
      And I select Gmail option
    When I enter Franco as name
      And I enter Aldunate as last name
      And I enter franco@gmail.com as user email
      And I enter pass123sADA_ as user password
      And I enter March as month birthday date
      And I enter 32 as day birthday date
      And I enter 2018 as year birthday date
      And I select Male as gender
      And I enter +59172493693 as phone number
      And I enter daniel@hotmail.com as current user email
      And I select Bolivia as location
    Then A new email account should be created