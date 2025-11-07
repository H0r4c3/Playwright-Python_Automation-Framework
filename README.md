# Playwright Python Test Automation Portfolio

******Author:****** Horatiu Crista
******Contact:****** dbmhorace@gmail.com

## 📋 Project Overview

This is a comprehensive test automation suite for the [Sauce Demo](https://www.saucedemo.com/) e-commerce website, built using **Playwright with Python** and **pytest**.

This project demonstrates professional test automation skills including:

- ✅ Page Object Model (POM) design pattern
- ✅ Pytest framework with fixtures and markers
- ✅ Organized test structure
- ✅ HTML test reports
- ✅ Parallel test execution
- ✅ Smoke and E2E test categorization

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **Playwright 1.49.1** - Browser automation
- **pytest 8.4.2** - Testing framework
- **pytest-playwright** - Playwright integration with pytest
- **pytest-html** - HTML test reports
- **pytest-xdist** - Parallel test execution

---

## 📁 Project Structure

```
portfolio_project/
├── tests/
│   ├── pages/                 # Page Object Model classes
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   └── cart_page.py
│   ├── test_login.py          # Login functionality tests
│   ├── test_products.py       # Products page tests
│   ├── test_cart.py           # Shopping cart tests
│   └── conftest.py            # Shared fixtures
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

---

**##** 🛠️ Development Tools

**###** Code Generation
**``**bash** **# Generate test code** **playwright codegen https://www.saucedemo.com** **``

**###** Debugging
**``**bash** **# Debug with inspector** **set**PWDEBUG**=**1** **pytest tests/test_login.py** **``**

**###** Trace Viewing
**``**bash** **# View test execution trace** **playwright show-trace test-results/trace-test_name.zip** **``

**###** Authentication State
**```**bash**
**# Save login state**
**python save_auth.py

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd portfolio_project
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest tests/ -v
```

### Run specific test file

```bash
pytest tests/test_login.py -v
```

### Run smoke tests only

```bash
pytest tests/ -v -m smoke
```

### Run E2E tests only

```bash
pytest tests/ -v -m e2e
```

### Run tests in parallel (faster)

```bash
pytest tests/ -v -n auto
```

### Generate HTML report

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

### Run in headless mode (no browser window)

```bash
pytest tests/ -v --headed=false
```

---

## 📊 Test Coverage

### Login Tests (5 tests)

- ✅ Successful login with valid credentials
- ✅ Login with locked out user
- ✅ Login with invalid username
- ✅ Login with invalid password
- ✅ Login with empty credentials

### Products Tests (7 tests)

- ✅ Products page loads correctly
- ✅ Add single product to cart
- ✅ Add multiple products to cart
- ✅ Sort products A to Z
- ✅ Sort products Z to A
- ✅ Sort products by price (low to high)
- ✅ Sort products by price (high to low)

### Cart Tests (6 tests)

- ✅ View empty cart
- ✅ View cart with items
- ✅ Remove item from cart
- ✅ Remove all items from cart
- ✅ Continue shopping from cart
- ✅ Full shopping flow (E2E test)

**Total: 18 automated tests**

## 🚀 Advanced Features

### API Testing

- ✅ GET, POST, PUT, DELETE requests
- ✅ Response validation
- ✅ Status code verification

### Performance Testing

- ✅ Page load time measurement
- ✅ DOM ready time tracking
- ✅ Performance thresholds validation

### Mobile Testing

- ✅ iPhone 12 responsive testing
- ✅ iPad Pro tablet testing
- ✅ Pixel 5 Android testing

### Visual Regression Testing

- ✅ Full page screenshot comparison
- ✅ Element-level visual testing
- ✅ Baseline image management

### Accessibility Testing

- ✅ Keyboard navigation
- ✅ Form label validation
- ✅ Heading structure verification

### Data-Driven Testing

- ✅ Parametrized test cases
- ✅ Multiple user scenarios
  **- ✅ Invalid input validation**

## 🎯 Extended Test Execution

**|** Command **|** Description **|**
**|**---------**|**-------------**|**
**|**`pytest tests/ -v -m api`**|** Run only API tests **|**
**|**`pytest tests/ -v -m performance`**|** Run performance tests **|**
**|**`pytest tests/ -v -m mobile`**|** Run mobile tests **|**
**|**`pytest tests/ -v -m visual`**|** Run visual regression tests **|**
**|**`pytest tests/ -v -m accessibility`**|** Run accessibility tests **|**

## 📊 Complete Test Statistics

**-****UI Tests:****** 18 tests
**-****API Tests:****** 4 tests
**-****Performance Tests:****** 2 tests
**-****Mobile Tests:****** 3 tests
**-****Visual Tests:****** 3 tests
**-****Accessibility Tests:****** 3 tests
**-****Data-Driven Tests:****** 7 tests

******Total: 40 automated tests****** across multiple testing categories!

---

## 🎯 Test Execution Options

| Command                              | Description                       |
| ------------------------------------ | --------------------------------- |
| `pytest tests/ -v`                 | Run all tests with verbose output |
| `pytest tests/ -v -m smoke`        | Run only smoke tests              |
| `pytest tests/ -v -m e2e`          | Run only end-to-end tests         |
| `pytest tests/ -v -n auto`         | Run tests in parallel             |
| `pytest tests/ --html=report.html` | Generate HTML report              |

---

## 📈 Sample Test Report

After running tests with `--html` flag, open `report.html` in your browser to see:

- Test execution summary
- Pass/fail status for each test
- Execution time
- Screenshots of failures
- Detailed error messages

---

## 🏗️ Design Patterns Used

### Page Object Model (POM)

Each page of the application has its own class containing:

- Locators for page elements
- Methods for page interactions
- Assertions for page verification

**Benefits:**

- Reusable code
- Easy maintenance
- Separation of test logic and page logic

### Fixtures (conftest.py)

Shared setup and teardown code using pytest fixtures:

- `login_page` - Provides LoginPage instance
- `products_page` - Provides ProductsPage instance
- `cart_page` - Provides CartPage instance
- `logged_in_user` - Pre-authenticated user session

## 📝 Notes

- Tests are designed to run independently
- Each test starts with a clean state
- Screenshots and videos are captured only on failures
- Compatible with CI/CD pipelines (GitHub Actions, Jenkins, etc.)

---

## 🔮 Future Enhancements

- [ ] Add API testing
- [ ] Implement visual regression testing
- [ ] Add database validation tests
- [ ] Integrate with CI/CD pipeline
- [ ] Add performance testing metrics
- [ ]

## 🛠️ Development Tools

**###** Code Generation
**``**bash** **# Generate test code** **playwright codegen https://www.saucedemo.com** **``

**###** Debugging
**``**bash** **# Debug with inspector** **set**PWDEBUG**=**1** **pytest tests/test_login.py** **``**

**###** Trace Viewing
**``**bash** **# View test execution trace** **playwright show-trace test-results/trace-test_name.zip** **``

**###** Authentication State
**```**bash**
**# Save login state**
**python save_auth.py

**# Tests use saved authentication (faster!)**

## 👤 Author

**Horatiu Crista**

- LinkedIn: [linkedin.com/in/horatiu-crista](https://www.linkedin.com/in/horatiu-crista)
- GitHub: [github.com/H0r4c3](https://github.com/H0r4c3)
- Email: dbmhorace@gmail.com

---
