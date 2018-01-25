import behave


@given(u'I enter {number:n} as quantity of habitants')
def step_impl(context, number):
    number_of_habitants = number
    print(number_of_habitants)


behave.use_step_matcher('re')


@given(u'I enter (?P<zip_value>[\d]*) as zip code')
def step_impl(context, zip_value):
    zip = zip_value
    print(zip)


@given(u'I enter (?P<country_value>[A-Za-z_]*) as country')
def step_impl(context, country_value):
    country = country_value
    print(country)
