# Created by tapes at 9/12/17
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: # Enter scenario name here
    # Enter steps here
#    Given sample tags
#    When we fetch the /tags url
#    Then we get a list of tags

    Given I have selected a recipe
    And it has a list of tags containing "foo"
    When I delete "foo"
    Then I do not see "foo" in the list of tags for this recipe