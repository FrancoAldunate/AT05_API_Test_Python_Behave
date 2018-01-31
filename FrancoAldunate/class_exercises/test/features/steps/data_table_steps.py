from compare import expect


@given(u'I select these artists')
def step_impl(context):
    context.ls = []
    for row in context.table:
        context.ls.append(row['name'])


@when(u'I choose option search')
def step_impl(context):
    a = 1


@then(u'A list of songs of each artist should be shown')
def step_impl(context):
    expect(context.ls[0]).to_equal('Michael Jackson')
