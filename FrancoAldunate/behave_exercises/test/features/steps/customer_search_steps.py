from AT05_API_Test_Python_Behave.FrancoAldunate.behave_exercises.customer.customer_info import Customer
from compare import expect


@when(u'I search for the customer')
def step_impl(context):
    customer = Customer()
    context.search_result = customer.is_client_name_found(context.name)


@then(u'The customer should be present in the customer\'s list')
def step_impl(context):
    expect(context.search_result).to_be_truthy()
