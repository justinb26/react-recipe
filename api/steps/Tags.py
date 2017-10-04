import requests
from behave import *

API_RECIPES = "http://localhost:8000/api/recipes"

use_step_matcher("parse")

@given("I have selected a recipe")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.recipe = requests.get(API_RECIPES).json()


@step('it has a list of tags containing "{tagname}"')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    assert(tagname in context.recipe[0]["tags"])


@when('I delete "{tagname}"')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    requests.delete


@then('I do not see "{tagname}" in the list of tags for this recipe')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    pass