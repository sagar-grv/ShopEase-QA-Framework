# ShopEase QA Automation Framework

Automation testing framework built using Selenium WebDriver, Python, PyTest, and Page Object Model (POM) for validating e-commerce workflows on SauceDemo.

## Features

* Login Automation Testing
* Cart Validation Testing
* Checkout Workflow Testing
* Positive and Negative Test Scenarios
* HTML Test Reports
* Reusable Page Object Model Structure

## Tech Stack

* Python
* Selenium
* PyTest
* PyTest HTML Reports
* Page Object Model (POM)

## Automated Test Cases

1. Valid Login
2. Invalid Login
3. Blank Username Validation
4. Blank Password Validation
5. Add Product To Cart
6. Remove Product From Cart
7. Successful Checkout
8. Blank Checkout Validation

## Test Execution

```bash
pytest -v
```

## Generate Report

```bash
pytest --html=reports/final_report.html
```
