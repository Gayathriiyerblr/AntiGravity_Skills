"""
OrangeHRM Login Page — Full Test Suite
Target URL : https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
Elements   : Username field | Password field | Login button
Coverage   : Positive | Negative | Boundary | Security | UX/UI  (30 TCs)
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

# ─────────────────────────────────────────────────────────────────────────────
# Test Data
# ─────────────────────────────────────────────────────────────────────────────

VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"


# ─────────────────────────────────────────────────────────────────────────────
# ✅  Positive Test Cases  (TC-LOGIN-001 to TC-LOGIN-005)
# ─────────────────────────────────────────────────────────────────────────────

class TestPositiveLogin:

    @pytest.mark.positive
    def test_TC_LOGIN_001_valid_credentials_redirect_to_dashboard(self, driver):
        """TC-LOGIN-001: Valid credentials → redirect to dashboard."""
        page = LoginPage(driver)
        page.login(VALID_USERNAME, VALID_PASSWORD)
        assert page.is_dashboard_loaded(), (
            f"Expected dashboard URL but got: {page.get_current_url()}"
        )

    @pytest.mark.positive
    def test_TC_LOGIN_002_enter_key_submits_form(self, driver):
        """TC-LOGIN-002: Pressing Enter on password field submits the form."""
        page = LoginPage(driver)
        page.submit_with_enter(VALID_USERNAME, VALID_PASSWORD)
        assert page.is_dashboard_loaded(), (
            "Enter key did not submit the form — dashboard not loaded."
        )

    @pytest.mark.positive
    def test_TC_LOGIN_003_alphanumeric_password_accepted(self, driver):
        """TC-LOGIN-003: Alphanumeric password is accepted on valid login."""
        page = LoginPage(driver)
        page.login(VALID_USERNAME, VALID_PASSWORD)   # admin123 is alphanumeric
        assert page.is_dashboard_loaded()

    @pytest.mark.positive
    def test_TC_LOGIN_004_page_loads_correctly(self, driver):
        """TC-LOGIN-005: Login page renders all key elements."""
        page = LoginPage(driver)
        assert page.get_username_field().is_displayed(), "Username field not visible"
        assert page.get_password_field().is_displayed(), "Password field not visible"
        assert page.get_login_button().is_displayed(),   "Login button not visible"

    @pytest.mark.positive
    def test_TC_LOGIN_005_page_title_contains_orangehrm(self, driver):
        """TC-LOGIN-030: Browser tab title contains 'OrangeHRM'."""
        page = LoginPage(driver)
        title = page.get_page_title()
        assert "OrangeHRM" in title, f"Expected 'OrangeHRM' in title, got: '{title}'"


# ─────────────────────────────────────────────────────────────────────────────
# ❌  Negative Test Cases  (TC-LOGIN-006 to TC-LOGIN-015)
# ─────────────────────────────────────────────────────────────────────────────

class TestNegativeLogin:

    @pytest.mark.negative
    def test_TC_LOGIN_006_invalid_username_valid_password(self, driver):
        """TC-LOGIN-006: Invalid username + valid password → error message."""
        page = LoginPage(driver)
        page.login("wronguser", VALID_PASSWORD)
        error = page.get_error_message()
        assert "Invalid credentials" in error, f"Unexpected error text: '{error}'"
        assert not page.is_dashboard_loaded()

    @pytest.mark.negative
    def test_TC_LOGIN_007_valid_username_invalid_password(self, driver):
        """TC-LOGIN-007: Valid username + invalid password → error message."""
        page = LoginPage(driver)
        page.login(VALID_USERNAME, "wrongpass")
        error = page.get_error_message()
        assert "Invalid credentials" in error, f"Unexpected error text: '{error}'"
        assert not page.is_dashboard_loaded()

    @pytest.mark.negative
    def test_TC_LOGIN_008_both_invalid_credentials(self, driver):
        """TC-LOGIN-008: Both invalid → error message shown."""
        page = LoginPage(driver)
        page.login("baduser", "badpass")
        error = page.get_error_message()
        assert "Invalid credentials" in error, f"Unexpected error text: '{error}'"

    @pytest.mark.negative
    def test_TC_LOGIN_009_empty_username(self, driver):
        """TC-LOGIN-009: Empty username → 'Required' validation error."""
        page = LoginPage(driver)
        page.login("", VALID_PASSWORD)
        errors = page.get_required_field_errors()
        assert any("Required" in e for e in errors), (
            f"Expected 'Required' error for username. Got: {errors}"
        )

    @pytest.mark.negative
    def test_TC_LOGIN_010_empty_password(self, driver):
        """TC-LOGIN-010: Empty password → 'Required' validation error."""
        page = LoginPage(driver)
        page.login(VALID_USERNAME, "")
        errors = page.get_required_field_errors()
        assert any("Required" in e for e in errors), (
            f"Expected 'Required' error for password. Got: {errors}"
        )

    @pytest.mark.negative
    def test_TC_LOGIN_011_both_fields_empty(self, driver):
        """TC-LOGIN-011: Both fields empty → two 'Required' validation errors."""
        page = LoginPage(driver)
        page.login("", "")
        errors = page.get_required_field_errors()
        assert len(errors) >= 2, (
            f"Expected at least 2 'Required' errors. Got {len(errors)}: {errors}"
        )

    @pytest.mark.negative
    def test_TC_LOGIN_012_spaces_only_username(self, driver):
        """TC-LOGIN-012: Spaces-only username → login does not succeed."""
        page = LoginPage(driver)
        page.login("   ", VALID_PASSWORD)
        assert not page.is_dashboard_loaded(), "Spaces-only username should not allow login"

    @pytest.mark.negative
    def test_TC_LOGIN_013_spaces_only_password(self, driver):
        """TC-LOGIN-013: Spaces-only password → login does not succeed."""
        page = LoginPage(driver)
        page.login(VALID_USERNAME, "   ")
        assert not page.is_dashboard_loaded(), "Spaces-only password should not allow login"

    @pytest.mark.negative
    def test_TC_LOGIN_014_case_sensitive_username(self, driver):
        """TC-LOGIN-014: Lowercase 'admin' (wrong case) → verify case sensitivity."""
        page = LoginPage(driver)
        page.login("admin", VALID_PASSWORD)
        # OrangeHRM is case-sensitive; lowercase 'admin' should fail
        assert not page.is_dashboard_loaded(), (
            "Login should fail with lowercase username 'admin' (case-sensitive system)"
        )

    @pytest.mark.negative
    def test_TC_LOGIN_015_numeric_username(self, driver):
        """TC-LOGIN-015: Numeric string as username → login fails."""
        page = LoginPage(driver)
        page.login("12345", VALID_PASSWORD)
        assert not page.is_dashboard_loaded()
        error = page.get_error_message()
        assert "Invalid credentials" in error


# ─────────────────────────────────────────────────────────────────────────────
# 🔢  Boundary Test Cases  (TC-LOGIN-016 to TC-LOGIN-020)
# ─────────────────────────────────────────────────────────────────────────────

class TestBoundaryLogin:

    @pytest.mark.boundary
    def test_TC_LOGIN_016_username_max_length_255_chars(self, driver):
        """TC-LOGIN-016: 255-character username → no crash; graceful error."""
        page = LoginPage(driver)
        long_username = "A" * 255
        page.login(long_username, VALID_PASSWORD)
        assert not page.is_dashboard_loaded(), "255-char username should not login successfully"

    @pytest.mark.boundary
    def test_TC_LOGIN_017_password_max_length_255_chars(self, driver):
        """TC-LOGIN-017: 255-character password → no crash; graceful error."""
        page = LoginPage(driver)
        long_password = "a" * 255
        page.login(VALID_USERNAME, long_password)
        assert not page.is_dashboard_loaded(), "255-char password should not login successfully"

    @pytest.mark.boundary
    def test_TC_LOGIN_018_username_single_char(self, driver):
        """TC-LOGIN-018: Single-character username → graceful error, no crash."""
        page = LoginPage(driver)
        page.login("A", VALID_PASSWORD)
        assert not page.is_dashboard_loaded()
        # No browser crash or unhandled exception expected

    @pytest.mark.boundary
    def test_TC_LOGIN_019_password_single_char(self, driver):
        """TC-LOGIN-019: Single-character password → graceful error, no crash."""
        page = LoginPage(driver)
        page.login(VALID_USERNAME, "a")
        assert not page.is_dashboard_loaded()

    @pytest.mark.boundary
    def test_TC_LOGIN_020_unicode_characters_in_fields(self, driver):
        """TC-LOGIN-020: Unicode characters in both fields → no crash."""
        page = LoginPage(driver)
        page.login("测试用户", "パスワード123")
        assert not page.is_dashboard_loaded(), (
            "Unicode credentials should not authenticate"
        )


# ─────────────────────────────────────────────────────────────────────────────
# 🔒  Security Test Cases  (TC-LOGIN-021 to TC-LOGIN-025)
# ─────────────────────────────────────────────────────────────────────────────

class TestSecurityLogin:

    @pytest.mark.security
    @pytest.mark.parametrize("sql_payload", [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "' OR 1=1 --",
        "admin'--",
    ])
    def test_TC_LOGIN_021_022_sql_injection_username(self, driver, sql_payload):
        """TC-LOGIN-021/022: SQL injection in username/password → login must fail."""
        page = LoginPage(driver)
        page.login(sql_payload, sql_payload)
        assert not page.is_dashboard_loaded(), (
            f"SQL injection payload should NOT result in login: '{sql_payload}'"
        )

    @pytest.mark.security
    @pytest.mark.parametrize("xss_payload", [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>",
        "javascript:alert('xss')",
    ])
    def test_TC_LOGIN_023_xss_injection_username(self, driver, xss_payload):
        """TC-LOGIN-023: XSS payloads in username → script must not execute."""
        page = LoginPage(driver)
        page.login(xss_payload, "anything")
        assert not page.is_dashboard_loaded(), (
            f"XSS payload should NOT result in login: '{xss_payload}'"
        )
        # Verify no JS alert was triggered
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.dismiss()
            pytest.fail(f"XSS alert was triggered with text: '{alert_text}'")
        except Exception:
            pass  # No alert = expected behaviour

    @pytest.mark.security
    def test_TC_LOGIN_024_password_field_is_masked(self, driver):
        """TC-LOGIN-024: Password field type attribute must be 'password'."""
        page = LoginPage(driver)
        pw_field = page.get_password_field()
        field_type = pw_field.get_attribute("type")
        assert field_type == "password", (
            f"Password field type should be 'password', got '{field_type}'"
        )

    @pytest.mark.security
    def test_TC_LOGIN_025_credentials_not_in_url_after_login(self, driver):
        """TC-LOGIN-025: URL after login must not expose credentials."""
        page = LoginPage(driver)
        page.login(VALID_USERNAME, VALID_PASSWORD)
        page.is_dashboard_loaded()
        current_url = page.get_current_url()
        assert VALID_USERNAME not in current_url, "Username exposed in URL"
        assert VALID_PASSWORD not in current_url, "Password exposed in URL"


# ─────────────────────────────────────────────────────────────────────────────
# 🎨  UX / UI Test Cases  (TC-LOGIN-026 to TC-LOGIN-030)
# ─────────────────────────────────────────────────────────────────────────────

class TestUXLogin:

    @pytest.mark.ux
    def test_TC_LOGIN_026_tab_navigation_order(self, driver):
        """TC-LOGIN-026: Tab key moves focus username → password → login button."""
        page = LoginPage(driver)

        username_field = page.get_username_field()
        username_field.click()
        username_field.send_keys(Keys.TAB)

        active_element = driver.switch_to.active_element
        pw_field = page.get_password_field()
        assert active_element == pw_field, "Tab from username should focus password field"

        active_element.send_keys(Keys.TAB)
        active_after_pw = driver.switch_to.active_element
        login_btn = page.get_login_button()
        assert active_after_pw == login_btn, "Tab from password should focus Login button"

    @pytest.mark.ux
    def test_TC_LOGIN_027_error_message_is_visible_and_non_empty(self, driver):
        """TC-LOGIN-027: Error message is displayed and not empty after failed login."""
        page = LoginPage(driver)
        page.login("wronguser", "wrongpass")
        error_text = page.get_error_message()
        assert error_text, "Error message should not be empty"
        assert len(error_text.strip()) > 0, "Error message text is blank"

    @pytest.mark.ux
    def test_TC_LOGIN_028_login_button_is_enabled_by_default(self, driver):
        """TC-LOGIN-029: Login button is enabled/clickable without entering any data."""
        page = LoginPage(driver)
        btn = page.get_login_button()
        assert btn.is_enabled(), "Login button should be enabled by default"
        assert btn.is_displayed(), "Login button should be visible on page load"

    @pytest.mark.ux
    def test_TC_LOGIN_029_username_field_is_editable(self, driver):
        """UI: Username field accepts keyboard input."""
        page = LoginPage(driver)
        field = page.get_username_field()
        field.send_keys("TestInput")
        assert field.get_attribute("value") == "TestInput"

    @pytest.mark.ux
    def test_TC_LOGIN_030_password_field_is_editable_and_masked(self, driver):
        """TC-LOGIN-024+UI: Password field accepts input and remains masked."""
        page = LoginPage(driver)
        field = page.get_password_field()
        field.send_keys("mypassword")
        assert field.get_attribute("type") == "password", "Password must be masked"
        assert field.get_attribute("value") == "mypassword", "Value should be stored"
