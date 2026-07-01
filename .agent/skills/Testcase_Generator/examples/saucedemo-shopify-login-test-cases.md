# Sauce Demo Shopify — Customer Login Page Test Cases

**Target URL:** https://sauce-demo.myshopify.com/account/login  
**Site Name:** simple. (Sauce Demo Shopify Store)  
**Page Heading:** Customer Login

---

## 🖥️ UI Analysis (from Screenshot)

| Element | Type | Details |
|---|---|---|
| **Email Address** | Text input (email) | Label above field, full-width, no placeholder |
| **Password** | Password input | Label above field, full-width, masked |
| **Forgot your password?** | Hyperlink | Below password field, left-aligned |
| **SIGN IN** | Submit button | Uppercase, outlined border style |
| **Sign up** | Header link | In top nav — links to registration |
| **No "Remember me"** | — | Not present on the form |
| **No inline register link** | — | Only available via header "Sign up" |

---

## 📊 Summary

| Metric | Count |
|---|---|
| **Total Test Cases** | 35 |
| **High Priority** | 14 |
| **Medium Priority** | 14 |
| **Low Priority** | 7 |
| **Positive** | 5 |
| **Negative** | 12 |
| **Boundary** | 8 |
| **Security** | 5 |
| **UX / UI** | 5 |

---

## ✅ Positive Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-SSDEMO-001 | Successful login with valid registered email and password | User is on the Customer Login page with a registered account | 1. Enter valid email<br>2. Enter correct password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `ValidPass@123` | User is redirected to the account dashboard/home page. No error displayed | High |
| TC-SSDEMO-002 | SIGN IN button submits form via Enter key on password field | User has entered valid credentials | 1. Enter valid email<br>2. Enter valid password<br>3. Press **Enter** in password field | Email: `testuser@example.com`<br>Password: `ValidPass@123` | Form submits; user is redirected to account page — same as clicking SIGN IN | High |
| TC-SSDEMO-003 | Email field accepts standard email format | User is on the login page | 1. Enter a properly formatted email address<br>2. Enter valid password<br>3. Click **SIGN IN** | Email: `user.name+tag@domain.co.uk`<br>Password: `ValidPass@123` | System accepts the email format; login proceeds without format error | Medium |
| TC-SSDEMO-004 | Login page loads all elements correctly | Browser is open | 1. Navigate to the login URL | URL: `https://sauce-demo.myshopify.com/account/login` | Page renders with: Email Address field, Password field, "Forgot your password?" link, SIGN IN button, site header & footer | High |
| TC-SSDEMO-005 | "Forgot your password?" link navigates to password reset page | User is on the login page | 1. Click **Forgot your password?** link | — | User is redirected to the password recovery/reset page | Medium |

---

## ❌ Negative Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-SSDEMO-006 | Login with unregistered email address | User is on the login page | 1. Enter an email not registered on the site<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `notregistered@fake.com`<br>Password: `anyPassword1` | Error message displayed (e.g., *"Invalid email or password"*). User stays on login page | High |
| TC-SSDEMO-007 | Login with valid email but wrong password | User is on the login page | 1. Enter a registered email<br>2. Enter incorrect password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `WrongPass999` | Error message displayed (e.g., *"Invalid email or password"*). User stays on login page | High |
| TC-SSDEMO-008 | Login with both email and password fields empty | User is on the login page | 1. Leave both fields blank<br>2. Click **SIGN IN** | Email: *(empty)*<br>Password: *(empty)* | Validation error shown for both fields; form is not submitted | High |
| TC-SSDEMO-009 | Login with empty email field only | User is on the login page | 1. Leave email field blank<br>2. Enter any password<br>3. Click **SIGN IN** | Email: *(empty)*<br>Password: `anyPassword1` | Validation error shown for the email field (e.g., *"Email can't be blank"*) | High |
| TC-SSDEMO-010 | Login with empty password field only | User is on the login page | 1. Enter a valid email<br>2. Leave password blank<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: *(empty)* | Validation error shown for the password field (e.g., *"Password can't be blank"*) | High |
| TC-SSDEMO-011 | Login with invalid email format (missing @ symbol) | User is on the login page | 1. Enter malformed email<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `testuserexample.com`<br>Password: `anyPassword1` | Browser or form validation rejects email — error message shown; no submission | High |
| TC-SSDEMO-012 | Login with invalid email format (missing domain) | User is on the login page | 1. Enter partial email<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `testuser@`<br>Password: `anyPassword1` | Validation error shown — invalid email format rejected | Medium |
| TC-SSDEMO-013 | Login with email containing spaces | User is on the login page | 1. Enter email with leading/trailing spaces<br>2. Enter valid password<br>3. Click **SIGN IN** | Email: `  testuser@example.com  `<br>Password: `ValidPass@123` | System either trims spaces and logs in, or shows format validation error. Login must not silently fail | Medium |
| TC-SSDEMO-014 | Login with spaces-only in password field | User is on the login page | 1. Enter valid email<br>2. Enter spaces as password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `     ` | Validation error or *"Invalid email or password"*. Login does not succeed | Medium |
| TC-SSDEMO-015 | Login with numeric-only email (no domain) | User is on the login page | 1. Enter numeric string as email<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `1234567890`<br>Password: `anyPassword1` | Format validation error — numeric string is not a valid email | Medium |
| TC-SSDEMO-016 | Login with correct email in different case | User is on the login page | 1. Enter registered email in all-caps<br>2. Enter correct password<br>3. Click **SIGN IN** | Email: `TESTUSER@EXAMPLE.COM`<br>Password: `ValidPass@123` | Verify case sensitivity behaviour — either login succeeds (case-insensitive email) or error is shown | Medium |
| TC-SSDEMO-017 | Login with previously used / expired session | User was previously logged in and session has expired | 1. Navigate directly to a protected page URL | — | User is redirected back to the Customer Login page; no access to protected content | High |

---

## 🔢 Boundary Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-SSDEMO-018 | Email field at maximum length (254 chars — RFC 5321 limit) | User is on the login page | 1. Enter a 254-character email address<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `a` × 243 + `@example.com` (254 chars total)<br>Password: `Test@1234` | System handles gracefully — either accepts or rejects with clear error. No crash | Medium |
| TC-SSDEMO-019 | Email field exceeding maximum length (255+ chars) | User is on the login page | 1. Enter a 300-character email string<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `a` × 289 + `@example.com` (301 chars)<br>Password: `Test@1234` | Field truncates input or shows validation error. No crash or server error | Medium |
| TC-SSDEMO-020 | Password at minimum length (1 character) | User is on the login page | 1. Enter a valid email<br>2. Enter single character password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `a` | Login fails with *"Invalid email or password"*. No crash | Medium |
| TC-SSDEMO-021 | Password at maximum length (255 characters) | User is on the login page | 1. Enter valid email<br>2. Enter 255-character password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `a` × 255 | System handles gracefully — either accepts (if password matches) or shows error. No crash | Medium |
| TC-SSDEMO-022 | Password exceeding maximum length (256+ characters) | User is on the login page | 1. Enter valid email<br>2. Paste 300-character string in password field<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `a` × 300 | Field truncates or shows validation error. No crash or 500 error | Medium |
| TC-SSDEMO-023 | Email with exactly 1 character before @ symbol | User is on the login page | 1. Enter minimum-valid local-part email<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `a@example.com`<br>Password: `Test@1234` | System accepts the email format (single-char local part is valid per RFC). Proceeds to authentication | Low |
| TC-SSDEMO-024 | Password with only special characters | User is on the login page | 1. Enter valid email<br>2. Enter all-special-character password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `!@#$%^&*()_+` | System handles gracefully — either invalid credentials or format error. No crash | Low |
| TC-SSDEMO-025 | Password field with Unicode/emoji characters | User is on the login page | 1. Enter valid email<br>2. Enter Unicode/emoji password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `🔑パスワード123` | System handles gracefully — error shown. No crash or data corruption | Low |

---

## 🔒 Security Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-SSDEMO-026 | SQL injection in email field | User is on the login page | 1. Enter SQL payload in email field<br>2. Enter any value in password<br>3. Click **SIGN IN** | Email: `' OR '1'='1' --`<br>Password: `anything` | Login fails; no SQL error exposed in UI or page source. Error: *"Invalid email or password"* | High |
| TC-SSDEMO-027 | SQL injection in password field | User is on the login page | 1. Enter valid/any email<br>2. Enter SQL payload in password<br>3. Click **SIGN IN** | Email: `testuser@example.com`<br>Password: `' OR '1'='1` | Login fails; no SQL error or stack trace exposed | High |
| TC-SSDEMO-028 | XSS script injection in email field | User is on the login page | 1. Enter XSS payload in email<br>2. Enter any password<br>3. Click **SIGN IN** | Email: `<script>alert('XSS')</script>`<br>Password: `test123` | Script is not executed; payload sanitised or shown as plain text. No alert box fires | High |
| TC-SSDEMO-029 | Password field is masked (type=password) | User is on the login page | 1. Click on the Password field<br>2. Type any text and observe | Password: `MySecret123` | Characters display as dots/asterisks. Field `type` attribute must be `password` | High |
| TC-SSDEMO-030 | Credentials not exposed in URL after SIGN IN attempt | User has submitted the login form | 1. Enter credentials<br>2. Click **SIGN IN**<br>3. Inspect the browser address bar | Email: `testuser@example.com`<br>Password: `ValidPass@123` | Neither email nor password appear in the URL query string after form submission | Medium |

---

## 🎨 UX / UI Test Cases

| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-SSDEMO-031 | Tab key navigates Email → Password → SIGN IN button | User is on the login page | 1. Click Email field<br>2. Press **Tab**<br>3. Press **Tab** again<br>4. Press **Tab** once more | — | Focus moves in order: Email Address → Password → SIGN IN button → Forgot your password? link | Medium |
| TC-SSDEMO-032 | Error message is visible, descriptive, and correctly placed | User submits invalid credentials | 1. Enter wrong email and password<br>2. Click **SIGN IN** | Email: `wrong@test.com`<br>Password: `wrongpass` | Error message is displayed prominently on the page, is non-empty, and clearly communicates the failure reason | High |
| TC-SSDEMO-033 | SIGN IN button is visible and clickable on page load | User is on the login page | 1. Navigate to login URL<br>2. Observe SIGN IN button without entering data | — | SIGN IN button is rendered, visible, and clickable (not greyed out or hidden) by default | Medium |
| TC-SSDEMO-034 | Login page is responsive on mobile viewport (375×812) | Browser resized to iPhone SE viewport | 1. Open login page at 375×812 viewport<br>2. Observe layout | — | Email field, Password field, "Forgot your password?" link, and SIGN IN button all display without horizontal scroll. Layout is single-column | Medium |
| TC-SSDEMO-035 | "Sign up" header link navigates to registration page | User is on the login page | 1. Click **Sign up** in the top navigation bar | — | User is redirected to the customer registration/account creation page | Low |

---

## 📝 UI-Specific Observations (from Screenshot Analysis)

| Observation | Impact on Testing |
|---|---|
| Label reads **"Email Address"** (not "Username") | Email format validation is mandatory — plain text usernames should be rejected |
| **No placeholder text** in email or password fields | No hint-driven testing needed; pure label-based UX |
| **"Forgot your password?"** link is present | Must verify link is functional and navigates to reset page |
| **SIGN IN** is outlined/bordered (not filled button) | Verify button hover state changes (border/text colour) |
| **No "Remember me"** checkbox | No persistent session checkbox tests required |
| **Payment icons in footer** (Amex, Visa, Mastercard) | Visual regression test — icons should render correctly |
| **Social icons** (Facebook, Twitter, Instagram, Pinterest, RSS) | Each icon should link to correct social page (separate test scope) |
| **"Sign up"** only in header nav | Registration flow is out of scope for this login test suite |

---

> **Note:** Valid test credentials for `sauce-demo.myshopify.com` must be obtained by registering an account on the demo store before executing positive test cases.
