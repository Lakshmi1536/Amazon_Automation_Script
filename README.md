Amazon Website Automation Project using Selenium Python (POM)
GitHub Link:
“Lakshmi1536/Amazon_Automation_Script at https/github.com/Lakshmi1536/Amazon-Automation.git”
Project Description:
Aim to build a robust automation framework to run the Amazon website.
Scenario 1: Page Navigation Test
Objective: Verify that each page of the Amazon website loads properly.
Steps:
1.	Open the Amazon website.
2.	Click on each page link (e.g., Home, Today's Deals, Your Amazon.com, etc.).
3.	Verify that the corresponding page loads successfully.
Scenario 2: End-to-End Shopping Scenario
Objective: Validate the end-to-end shopping flow from product search to checkout.
Steps:
1.	Open the Amazon website.
2.	Search for a product using the search bar.
3.	Select the desired product from the search results.
4.	Verify that the product details page loads successfully.
5.	Explore all product images by clicking on each image thumbnail.
6.	Increase the quantity of the product.
7.	Add the product to the cart.
8.	Verify that the product is added to the cart successfully.
9.	Proceed to the checkout page.
10.	Verify that the checkout page loads successfully.
Scenario 3: Additional Scenarios
Objective: Test additional functionalities such as scrolling, mouse hover actions, and playing videos.
Steps:
1.	Open the Amazon website.
2.	Scroll down the page to verify smooth scrolling behavior.
3.	Hover the mouse over a product to trigger the hover action.
4.	Verify that product details are displayed on hover.
5.	Navigate to a page with a video (e.g., a product page with a product demonstration video).
6.	Click on the video to play it.
7.	Verify that the video starts playing successfully.
Page Object Model
The Page Object Model (POM) in Selenium is a design pattern aimed at minimizing code duplication and streamlining code update and maintenance processes. 
What is Page Object Model (POM)?
POM establishes an object repository for storing web elements.
It creates dedicated page classes for each webpage within your Automation Under Test (AUT).
The purpose is to minimize code repetition and enhance the maintenance of test cases.
By using POM, you can efficiently manage web elements, making your code more modular and maintainable.
How Does POM Work?
Page Class/Page Object: This class acts as an object repository for the web elements (UI elements) of the web pages under test.
It contains methods to perform operations on these web elements.
Changes in the UI elements require updates only in the Page Class, keeping the test code unchanged.
Test Cases: These contain the actual test scenarios.
Test cases use methods from the Page Class to interact with the UI.
When the UI changes, only the Page Class needs updating, while the test code remains stable1
Test case explanation: Scenario 1
Prerequisites: Landing on the Amazon website Home page
Page Scenario:
Testcase 1 “Fresh” Page tab Layout Checking
1.	Initialize WebDriver.
2.	Open the website.
3.	Use WebDriverWait to wait for the Fresh tab to be clickable and click on it.
4.	Assert the page title after clicking on the Fresh tab.
5.	Use WebDriverWait to wait for the pop-up close button to be clickable and click on it.
6.	Assert landing on the home page again after closing the pop-up.
7.	Print the test result.
8.	Finally, close the browser session.
Testcase 2 “MiniTv” Page tab Layout Checking
1.	Initialize WebDriver.
2.	Open the website.
3.	Use WebDriverWait to wait for the MiniTv tab to be clickable and click on it.
4.	Assert the page title after clicking on the MiniTv tab.
5.	Use WebDriverWait to wait for the pop-up close button to be clickable and click on it.
6.	Assert landing on the home page again after closing the pop-up.
7.	Print the test result.
8.	Finally, close the browser session.
Testcase 3 “Sell” Page tab Layout Checking
1.	Initialize WebDriver.
2.	Open the website.
3.	Use WebDriverWait to wait for the Sell tab to be clickable and click on it.
4.	Assert the page title after clicking on the Sell tab.
5.	Use WebDriverWait to wait for the pop-up close button to be clickable and click on it.
6.	Assert landing on the home page again after closing the pop-up.
7.	Print the test result.
8.	Finally, close the browser session.
Testcase 4 “Best Sellers” Page tab Layout Checking
1.	Initialize WebDriver.
2.	Open the website.
3.	Use WebDriverWait to wait for the Best Seller tab to be clickable and click on it.
4.	Assert the page title after clicking on the Best Seller tab.
5.	Use WebDriverWait to wait for the pop-up close button to be clickable and click on it.
6.	Assert landing on the home page again after closing the pop-up.
7.	Print the test result.
8.	Finally, close the browser session.
Testcase 5 “Today’s Deal” Page tab Layout Checking
1.	Initialize WebDriver.
2.	Open the website.
3.	Use WebDriverWait to wait for the Today’s Deal tab to be clickable and click on it.
4.	Assert the page title after clicking on the Today’s Deal tab.
5.	Use WebDriverWait to wait for the pop-up close button to be clickable and click on it.
6.	Assert landing on the home page again after closing the pop-up.
7.	Print the test result.
8.	Finally, close the browser session.

 

