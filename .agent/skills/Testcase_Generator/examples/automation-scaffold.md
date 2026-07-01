# Automation Scaffold — OrangeHRM Login Page
**Framework:** Pytest + Selenium WebDriver  
**Target URL:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

---

## Project Structure

```
tests/
├── conftest.py              # Driver setup & teardown
├── pages/
│   └── login_page.py        # Page Object Model for login
└── test_login.py            # Test cases mapped from login-test-cases.md
```

---

## conftest.py

```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment for headless mode
    drv = webdriver.Chrome(options=options)
    drv.get(BASE_URL)
    yield drv
    drv.quit()
```

---

## pages/login_page.py

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON   = (By.XPATH, "//button[@type='submit']")
    ERROR_ALERT    = (By.XPATH, "//div[contains(@class,'oxd-alert')]")
    REQUIRED_MSGS  = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username: str):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password: str):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_ALERT)).text

    def get_required_field_errors(self) -> list[str]:
        elements = self.wait.until(EC.presence_of_all_elements_located(self.REQUIRED_MSGS))
        return [el.text for el in elements]

    def is_dashboard_loaded(self) -> bool:
        return "/dashboard" in self.driver.current_url
```

---

## test_login.py

```python
import pytest
from pages.login_page import LoginPage

VALID_USER = "Admin"
VALID_PASS = "admin123"


# --- Positive Tests ---

class TestPositiveLogin:

    def test_tc_login_001_valid_credentials(self, driver):
        """TC-LOGIN-001: Successful login with valid credentials."""
        page = LoginPage(driver)
        page.login(VALID_USER, VALID_PASS)
        assert page.is_dashboard_loaded(), "Expected redirect to dashboard after valid login"

    def test_tc_login_002_enter_key_submits(self, driver):
        """TC-LOGIN-002: Login via Enter key."""
        from selenium.webdriver.common.keys import Keys
        page = LoginPage(driver)
        page.enter_username(VALID_USER)
        page.enter_password(VALID_PASS)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(Keys.RETURN)
        assert page.is_dashboard_loaded()


# --- Negative Tests ---

class TestNegativeLogin:

    @pytest.mark.parametrize("username,password", [
        ("wronguser", VALID_PASS),       # TC-LOGIN-006
        (VALID_USER, "wrongpass"),       # TC-LOGIN-007
        ("baduser",  "badpass"),         # TC-LOGIN-008
    ])
    def test_invalid_credentials(self, driver, username, password):
        """TC-LOGIN-006/007/008: Invalid credentials show error."""
        page = LoginPage(driver)
        page.login(username, password)
        error = page.get_error_message()
        assert "Invalid credentials" in error

    def test_tc_login_009_empty_username(self, driver):
        """TC-LOGIN-009: Empty username shows required error."""
        page = LoginPage(driver)
        page.login("", VALID_PASS)
        errors = page.get_required_field_errors()
        assert any("Required" in e for e in errors)

    def test_tc_login_010_empty_password(self, driver):
        """TC-LOGIN-010: Empty password shows required error."""
        page = LoginPage(driver)
        page.login(VALID_USER, "")
        errors = page.get_required_field_errors()
        assert any("Required" in e for e in errors)

    def test_tc_login_011_both_empty(self, driver):
        """TC-LOGIN-011: Both fields empty shows two required errors."""
        page = LoginPage(driver)
        page.login("", "")
        errors = page.get_required_field_errors()
        assert len(errors) >= 2


# --- Security Tests ---

class TestSecurityLogin:

    @pytest.mark.parametrize("payload", [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "<script>alert('XSS')</script>",
    ])
    def test_injection_payloads(self, driver, payload):
        """TC-LOGIN-021/022/023: Injection payloads should not succeed or crash."""
        page = LoginPage(driver)
        page.login(payload, payload)
        assert not page.is_dashboard_loaded(), "Injection payload should NOT result in login"

    def test_tc_login_024_password_masked(self, driver):
        """TC-LOGIN-024: Password field type should be 'password' (masked)."""
        page = LoginPage(driver)
        pw_field = driver.find_element(*LoginPage.PASSWORD_INPUT)
        assert pw_field.get_attribute("type") == "password"
```

---

## Running the Tests

```bash
# Install dependencies
pip install pytest selenium

# Run all tests
pytest tests/ -v

# Run only security tests
pytest tests/test_login.py::TestSecurityLogin -v

# Run with HTML report
pytest tests/ -v --html=report.html --self-contained-html
```

---

> **Note:** Ensure ChromeDriver matches your installed Chrome version.  
> Run `chromedriver --version` and `google-chrome --version` to verify compatibility.
