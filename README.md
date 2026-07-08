# UI Automation Framework — Python + Playwright

A Page Object Model (POM) based UI automation framework built with Python and Playwright, tested against [SauceDemo](https://www.saucedemo.com).

## Tech Stack
- Python 3.13
- Playwright (sync API)
- pytest
- pytest-html (HTML reporting)

## Project Structure
pages/              # Page Object classes (locators + actions per page)
├── login_page.py
├── inventory_page.py
└── cart_page.py
utils/
└── constants.py     # Centralized test data (URLs, credentials)
Test files (project root):
├── test_checkout_flow.py
├── test_verify_price.py
├── test_verify_description.py
├── test_remove_item.py
├── test_multiple_items.py
├── test_invalid_login.py
└── ... (10 tests total)

## Features Covered
- Login (valid and invalid credentials)
- Add/remove items from cart
- Cart badge count verification
- Product price and description verification
- Product navigation
- Full checkout flow navigation

## Running the Tests

Install dependencies:
```bash
pip3 install playwright pytest pytest-html
playwright install
```

Run all tests:
```bash
pytest -v
```

Run a specific test:
```bash
pytest test_checkout_flow.py -v
```

Generate an HTML report:
```bash
pytest --html=report.html --self-contained-html
```

## Design Notes
This framework follows the Page Object Model pattern — each page's locators and actions are encapsulated in its own class under `pages/`, keeping test files clean and readable. Test data is centralized in `utils/constants.py` to avoid duplication.