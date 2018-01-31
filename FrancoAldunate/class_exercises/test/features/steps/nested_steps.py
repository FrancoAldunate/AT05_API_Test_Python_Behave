@given(u'I have ${balance:d} in my account')
def step_impl(context, balance):
    a = 1


@given(u'I have authenticated with the correct PIN using slot {number}')
def step_impl(context, number):
    context.execute_steps('''
    Given I have pushed my card in the slot %s
    When I enter my PIN
      And I press "OK"''' % number)


@when(u'I choose to withdraw the fixed amount of ${withdraw:d}')
def step_impl(context, withdraw):
    a = 1


@then(u'I should receive ${cash} cash')
def step_impl(context, cash):
    a = 1


@then(u'the balance of my account should be ${result:d}')
def step_impl(context, result):
    a = 1
