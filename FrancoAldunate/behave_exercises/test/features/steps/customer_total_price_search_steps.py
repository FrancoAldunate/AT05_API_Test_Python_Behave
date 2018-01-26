from AT05_API_Test_Python_Behave.FrancoAldunate.behave_exercises.customer.customer_info import Customer
from compare import expect
import behave

behave.use_step_matcher('re')


@given(u'I enter (?P<name>[A-Za-z]+) as name of the client')
def step_impl(context, name):
    context.name = name


@given(u'I enter (?P<id>[\d]) as id of the client')
def step_impl(context, id):
    context.id = id


@given(u'I enter (?P<total_price>[\d]+) as the total price of purchase')
def step_impl(context, total_price):
    context.total_price = total_price


@when(u'I search for the customer total price')
def step_impl(context):
    customer = Customer()
    context.result = None
    context.key_by_name = customer.get_id_by_client_name(context.name)
    if context.key_by_name == int(context.id):
        context.result = customer.get_client_total_price_by_id(context.key_by_name)


@then(u'The total price should be found in the customer\'s total price list')
def step_impl(context):
    expect(context.result).to_equal(int(context.total_price))
