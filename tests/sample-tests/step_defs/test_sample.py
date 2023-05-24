from pytest_bdd import given, when, then, scenarios

scenarios("sample.feature", features_base_dir="tests/sample-tests/features/")

@given("I have a dummy step")
def i_have_a_dummy_step():
    pass

@when("I perform an action")
def i_perform_an_action():
    pass

@then("I expect a result")
def i_expect_a_result():
    assert True


@given("I dont have a dummy step")
def step_impl():
    raise NotImplementedError(u'STEP: Given I dont have a dummy step')


@when("I dont perform an action")
def step_impl():
    raise NotImplementedError(u'STEP: When I dont perform an action')


@then("I dont expect a result")
def step_impl():
    raise NotImplementedError(u'STEP: Then I dont expect a result')
