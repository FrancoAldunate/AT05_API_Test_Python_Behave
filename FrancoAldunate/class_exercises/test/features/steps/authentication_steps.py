@given(u'I have pushed my card in the slot {number}')
def step_impl(context, number):
    print(number)
    a = 1


@when(u'I enter my PIN')
def step_impl(context):
    a = 1


@when(u'I press "OK"')
def step_impl(context):
    a = 1


@then(u'I should see the main menu')
def step_impl(context):
    a = 1
