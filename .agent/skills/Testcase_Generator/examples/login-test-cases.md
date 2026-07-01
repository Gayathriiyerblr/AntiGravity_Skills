# OrangeHRM Login Page — Test Cases
**Target URL:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login  
**Elements Under Test:** Username field, Password field, Login button  
**Valid Credentials:** `Admin` / `admin123`

---

## 📊 Summary

| Metric | Count |
|---|---|
| **Total Test Cases** | 30 |
| **High Priority** | 12 |
| **Medium Priority** | 12 |
| **Low Priority** | 6 |
| **Positive** | 5 |
| **Negative** | 10 |
| **Boundary** | 5 |
| **Security** | 5 |
| **UX / UI** | 5 |

---

## ✅ Positive Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-LOGIN-001 | Successful login with valid credentials | User is on the login page | 1. Enter username<br>2. Enter password<br>3. Click **Login** | Username: `Admin`<br>Password: `admin123` | User is redirected to the OrangeHRM dashboard (`/dashboard/index`) | High |
| TC-LOGIN-002 | Login button submits form via Enter key | User has entered valid credentials | 1. Enter username<br>2. Enter password<br>3. Press **Enter** | Username: `Admin`<br>Password: `admin123` | User is redirected to the dashboard — same as clicking Login | High |
| TC-LOGIN-003 | Password field accepts alphanumeric password | User is on the login page | 1. Enter valid username<br>2. Enter alphanumeric password<br>3. Click **Login** | Username: `Admin`<br>Password: `admin123` | Login succeeds; dashboard loads | Medium |
| TC-LOGIN-004 | Session persists after login | User has logged in successfully | 1. Log in<br>2. Refresh the browser | Valid credentials | Session remains active; user stays on dashboard | Medium |
| TC-LOGIN-005 | Login page loads correctly | Browser is open | 1. Navigate to the login URL | URL: `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login` | Login page renders with username field, password field, and login button visible | High |

---

## ❌ Negative Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-LOGIN-006 | Login with invalid username and valid password | User is on the login page | 1. Enter invalid username<br>2. Enter valid password<br>3. Click **Login** | Username: `wronguser`<br>Password: `admin123` | Error message displayed: *"Invalid credentials"*. User stays on login page | High |
| TC-LOGIN-007 | Login with valid username and invalid password | User is on the login page | 1. Enter valid username<br>2. Enter wrong password<br>3. Click **Login** | Username: `Admin`<br>Password: `wrongpass` | Error message displayed: *"Invalid credentials"*. User stays on login page | High |
| TC-LOGIN-008 | Login with both invalid username and password | User is on the login page | 1. Enter invalid username<br>2. Enter invalid password<br>3. Click **Login** | Username: `baduser`<br>Password: `badpass` | Error message displayed: *"Invalid credentials"*. User stays on login page | High |
| TC-LOGIN-009 | Login with empty username field | User is on the login page | 1. Leave username blank<br>2. Enter valid password<br>3. Click **Login** | Username: *(empty)*<br>Password: `admin123` | Validation error shown below username field: *"Required"* | High |
| TC-LOGIN-010 | Login with empty password field | User is on the login page | 1. Enter valid username<br>2. Leave password blank<br>3. Click **Login** | Username: `Admin`<br>Password: *(empty)* | Validation error shown below password field: *"Required"* | High |
| TC-LOGIN-011 | Login with both fields empty | User is on the login page | 1. Leave both fields blank<br>2. Click **Login** | Username: *(empty)*<br>Password: *(empty)* | Validation errors shown for both fields; form not submitted | High |
| TC-LOGIN-012 | Login with spaces only in username | User is on the login page | 1. Enter spaces in username<br>2. Enter valid password<br>3. Click **Login** | Username: `   `<br>Password: `admin123` | Validation error or *"Invalid credentials"* — login does not succeed | Medium |
| TC-LOGIN-013 | Login with spaces only in password | User is on the login page | 1. Enter valid username<br>2. Enter spaces in password<br>3. Click **Login** | Username: `Admin`<br>Password: `   ` | Validation error or *"Invalid credentials"* — login does not succeed | Medium |
| TC-LOGIN-014 | Login with correct credentials in wrong case | User is on the login page | 1. Enter username in lowercase<br>2. Enter valid password<br>3. Click **Login** | Username: `admin`<br>Password: `admin123` | System handles case sensitivity — either logs in (if case-insensitive) or shows error | Medium |
| TC-LOGIN-015 | Login with numeric username | User is on the login page | 1. Enter a numeric string as username<br>2. Enter valid password<br>3. Click **Login** | Username: `12345`<br>Password: `admin123` | Error message: *"Invalid credentials"*. User stays on login page | Low |

---

## 🔢 Boundary Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-LOGIN-016 | Username at maximum character length | User is on the login page | 1. Enter a 255-character string in username<br>2. Enter any password<br>3. Click **Login** | Username: `A` × 255<br>Password: `admin123` | System handles gracefully — either trims, rejects, or shows error. No crash | Medium |
| TC-LOGIN-017 | Password at maximum character length | User is on the login page | 1. Enter valid username<br>2. Enter 255-character password<br>3. Click **Login** | Username: `Admin`<br>Password: `a` × 255 | System handles gracefully — error shown, no crash | Medium |
| TC-LOGIN-018 | Username with single character | User is on the login page | 1. Enter a 1-character username<br>2. Enter valid password<br>3. Click **Login** | Username: `A`<br>Password: `admin123` | Error message: *"Invalid credentials"*. No crash | Low |
| TC-LOGIN-019 | Password with single character | User is on the login page | 1. Enter valid username<br>2. Enter a 1-character password<br>3. Click **Login** | Username: `Admin`<br>Password: `a` | Error message: *"Invalid credentials"*. No crash | Low |
| TC-LOGIN-020 | Input fields accept Unicode/special characters | User is on the login page | 1. Enter Unicode characters in both fields<br>2. Click **Login** | Username: `测试用户`<br>Password: `パスワード` | System handles gracefully — error shown, no crash or data corruption | Medium |

---

## 🔒 Security Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-LOGIN-021 | SQL injection in username field | User is on the login page | 1. Enter SQL payload in username<br>2. Enter any password<br>3. Click **Login** | Username: `' OR '1'='1`<br>Password: `anything` | Login fails; no SQL error exposed. Error: *"Invalid credentials"* | High |
| TC-LOGIN-022 | SQL injection in password field | User is on the login page | 1. Enter valid username<br>2. Enter SQL payload in password<br>3. Click **Login** | Username: `Admin`<br>Password: `' OR '1'='1` | Login fails; no SQL error exposed | High |
| TC-LOGIN-023 | XSS script injection in username field | User is on the login page | 1. Enter XSS payload in username<br>2. Enter any password<br>3. Click **Login** | Username: `<script>alert('XSS')</script>`<br>Password: `test` | Script is not executed; payload is sanitized or shown as plain text | High |
| TC-LOGIN-024 | Password field input is masked | User is on the login page | 1. Click on the password field<br>2. Type any text | Password: `admin123` | Characters are displayed as dots/asterisks (masked) | High |
| TC-LOGIN-025 | Credentials not exposed in URL after login | User has submitted the login form | 1. Log in with valid credentials<br>2. Inspect the browser URL after redirect | Username: `Admin`<br>Password: `admin123` | URL does not contain username or password in query params | Medium |

---

## 🎨 UX / UI Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-LOGIN-026 | Tab key navigates from username → password → login button | User is on the login page | 1. Click username field<br>2. Press **Tab**<br>3. Press **Tab** again | — | Focus moves: Username → Password → Login Button in order | Medium |
| TC-LOGIN-027 | Error message is visible and descriptive | User has submitted invalid credentials | 1. Enter wrong credentials<br>2. Click **Login** | Username: `wrong`<br>Password: `wrong` | Error alert is visible, non-empty, and reads *"Invalid credentials"* | Medium |
| TC-LOGIN-028 | Login page is responsive on mobile viewport | Browser is resized to 375×812 (iPhone) | 1. Open login page at mobile viewport size | — | All elements (fields, button, logo) are visible and usable without horizontal scrolling | Low |
| TC-LOGIN-029 | Login button is clickable and not disabled by default | User is on the login page | 1. Navigate to login page<br>2. Do not enter any data<br>3. Observe Login button | — | Login button is visible, enabled, and clickable (validation fires on click, not before) | Medium |
| TC-LOGIN-030 | Page title and branding are correct | User is on the login page | 1. Navigate to login page<br>2. Check browser tab title and on-page logo | — | Page title contains "OrangeHRM"; OrangeHRM logo is displayed on the page | Low |

---

> **Reference Credential (Demo Site):** Username: `Admin` | Password: `admin123`  
> **Note:** The demo site resets periodically. Always verify credentials before running automated tests.
