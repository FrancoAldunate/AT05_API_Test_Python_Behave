import behave

behave.use_step_matcher('re')


@given(u'I go to www.google.com')
def step_impl(context):
    print("www.google.com")


@given(u'I select Gmail option')
def step_impl(context):
    print("Gmail")


@when(u'I enter (?P<name_value>[A-Za-z]+) as name')
def step_impl(context, name_value):
    print(name_value)


@when(u'I enter (?P<lastname_value>[A-Za-z]+) as last name')
def step_impl(context, lastname_value):
    print(lastname_value)


@when(u'I enter (?P<email_value>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,4}) as user email')
def step_impl(context, email_value):
    print(email_value)


@when(u'I enter (?P<password_value>[\w]{8,16}) as user password')
def step_impl(context, password_value):
    print(password_value)


@when(
    u'I enter (?P<month_value>January|February|March|April|June|July|August|September|October|November|December) as month birthday date')
def step_impl(context, month_value):
    print(month_value)


@when(u'I enter (?P<day_value>[0-3]*[\d]{1,2}) as day birthday date')
def step_impl(context, day_value):
    print(day_value)


@when(u'I enter (?P<year_value>19[\d]{2}|20[\d]{2}) as year birthday date')
def step_impl(context, year_value):
    print(year_value)


@when(u'I select (?P<gender_value>Male|Female|Other|Rather not to say) as gender')
def step_impl(context, gender_value):
    print(gender_value)


@when(u'I enter (?P<phone_number>\+[\d]{3}[\d]{8}) as phone number')
def step_impl(context, phone_number):
    print(phone_number)


@when(u'I enter (?P<current_email_value>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,4}) as current user email')
def step_impl(context, current_email_value):
    print(current_email_value)


@when(u'I select (?P<location_value>[A-Za-z]*) as location')
def step_impl(context, location_value):
    print(location_value)


@then(u'A new email account should be created')
def step_impl(context):
    print("Email created")
