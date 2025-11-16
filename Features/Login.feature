@smoke
Feature: To test the login page of the website


Scenario Outline: To test the login page of the website with multiple credentials
Given the user is one the login page of the sauce demo website
When the user puts in username "<username>" and password "<password>"
And the user clicks on the login button
Then the user gets navigated to the landing page of the website

Examples:
| username | password |
| standard_user | secret_sauce |
| problem_user | secret_sauce |
| performance_glitch_user | secret_sauce |
| error_user | secret_sauce |
| visual_user | secret_sauce |
