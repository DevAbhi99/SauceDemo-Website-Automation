Feature: To test the main checkout flow of the website

Scenario: To test checkout flow of the website with correct inputs

Given the user is on the landing page of the website
When the user is on the landing page then the user clicks on add to cart of a button and proceed to click on the shopping cart button
And the user is navigated to the checkout page where the user clicks on the checkout button
When the user is navigated to the information page then the user is provides valid information and clicks on continue button
And the the user is navigated to the description page where the user has to click on the Finish button
When the user is navigated to final checkout page and the user clicks on the Back home button
Then the user is navigated back to landing page of the website