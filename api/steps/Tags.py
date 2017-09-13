import requests
from behave import *

use_step_matcher("re")




@given("sample tags")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Populate db with tags
    pass


@when("we fetch the /tags url")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    testurl = "http://localhost:8000/api/tags"
    # Fetch tags
    context.r = requests.get(testurl)


@then("we get a list of tags")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    results = context.r.json()
    assert len(results) > 0

