from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object Model for the OrangeHRM Login Page.
    URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    """

    # ── Locators ──────────────────────────────────────────────────────────────
    USERNAME_INPUT   = (By.NAME,  "username")
    PASSWORD_INPUT   = (By.NAME,  "password")
    LOGIN_BUTTON     = (By.XPATH, "//button[@type='submit']")
    ERROR_ALERT      = (By.XPATH, "//div[contains(@class,'oxd-alert-content')]//p")
    REQUIRED_MSGS    = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")
    DASHBOARD_HEADER = (By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb')]")

    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, self.TIMEOUT)

    # ── Actions ───────────────────────────────────────────────────────────────

    def enter_username(self, username: str):
        """Clear and type into the username field."""
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password: str):
        """Clear and type into the password field."""
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        """Click the Login submit button."""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username: str, password: str):
        """Convenience: enter credentials and submit."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def submit_with_enter(self, username: str, password: str):
        """Enter credentials and press Enter key to submit."""
        self.enter_username(username)
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)
        field.send_keys(Keys.RETURN)

    # ── Assertions / Queries ──────────────────────────────────────────────────

    def is_dashboard_loaded(self) -> bool:
        """Return True if the dashboard URL is active."""
        try:
            self.wait.until(EC.url_contains("/dashboard"))
            return True
        except Exception:
            return False

    def get_error_message(self) -> str:
        """Return the text of the login error alert."""
        element = self.wait.until(EC.visibility_of_element_located(self.ERROR_ALERT))
        return element.text.strip()

    def get_required_field_errors(self) -> list:
        """Return a list of all 'Required' field validation messages."""
        self.wait.until(EC.presence_of_element_located(self.REQUIRED_MSGS))
        elements = self.driver.find_elements(*self.REQUIRED_MSGS)
        return [el.text.strip() for el in elements]

    def get_username_field(self):
        """Return the username WebElement."""
        return self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))

    def get_password_field(self):
        """Return the password WebElement."""
        return self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))

    def get_login_button(self):
        """Return the Login button WebElement."""
        return self.wait.until(EC.presence_of_element_located(self.LOGIN_BUTTON))

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self) -> str:
        return self.driver.title
