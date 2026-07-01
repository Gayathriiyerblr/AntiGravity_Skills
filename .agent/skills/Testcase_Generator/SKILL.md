---
name: generating-test-cases
description: >
  Generates structured, comprehensive test cases for web application UI components and workflows.
  Use this skill when the user mentions: "create test cases", "write test scenarios", "generate tests",
  "test coverage", "login page testing", "form validation testing", or references a URL with UI elements
  like input fields, buttons, and forms. Covers positive, negative, boundary, security, and UX scenarios.
---

# Test Case Generator

## When to Use This Skill

- User provides a URL or describes a UI with input fields, buttons, or forms
- User asks to "generate", "write", or "create" test cases
- User mentions a feature to test (e.g., login, registration, search, checkout)
- User wants test coverage analysis or scenario planning

---

## Workflow

Use this checklist for every test case generation request:

- [ ] **1. Understand the target** — URL, component list, and expected behavior
- [ ] **2. Identify input elements** — text fields, dropdowns, checkboxes, buttons
- [ ] **3. Define test categories** — Positive / Negative / Boundary / Security / UX
- [ ] **4. Write test cases** using the standard template below
- [ ] **5. Review edge cases** — empty inputs, special characters, long strings, SQL/XSS
- [ ] **6. Output** — Deliver as markdown table or structured list per user preference

---

## Instructions

### Step 1 — Gather Context

Before generating, confirm:
- Target URL or feature description
- UI elements present (e.g., username field, password field, login button)
- Any known valid/invalid credentials or data constraints
- Test framework preference (manual / Selenium / Playwright / Cypress / Pytest)

---

### Step 2 — Test Case Template

Use this structure for each test case:

```
| TC-ID | Test Scenario | Precondition | Test Steps | Test Data | Expected Result | Priority |
```

**Field Definitions:**
- **TC-ID**: Sequential ID, e.g., `TC-LOGIN-001`
- **Test Scenario**: One-line description of what is being tested
- **Precondition**: State required before execution (e.g., "User is on the login page")
- **Test Steps**: Numbered action steps
- **Test Data**: Exact input values used
- **Expected Result**: Specific observable outcome
- **Priority**: `High` / `Medium` / `Low`

---

### Step 3 — Category Coverage

Always cover these categories in order:

#### ✅ Positive Test Cases
- Valid credentials → successful outcome
- Alternative valid formats (e.g., case sensitivity if supported)

#### ❌ Negative Test Cases
- Invalid credentials
- Empty required fields (individual + all at once)
- Wrong data types (numbers where text expected, etc.)
- Incorrect formats

#### 🔢 Boundary Test Cases
- Max-length input values
- Min-length input values (e.g., 1 character)
- Exactly at boundary (e.g., exactly 255 chars)

#### 🔒 Security Test Cases
- SQL injection payloads in input fields
- XSS script injection
- Password field masking verification
- Credential exposure in URL or page source

#### 🎨 UX / UI Test Cases
- Tab key navigation order
- Enter key form submission
- Error message visibility, content, and placement
- Button enabled/disabled states
- Page responsiveness

---

### Step 4 — Output Format Rules

- Group test cases by category with clear headings
- Use a markdown table for easy readability
- Include a **Summary Stats block** at the top:

```
Total TCs: XX  |  High: X  |  Medium: X  |  Low: X
Positive: X  |  Negative: X  |  Boundary: X  |  Security: X  |  UX: X
```

- For automation frameworks, append a code scaffold at the end
- See [examples/login-test-cases.md](examples/login-test-cases.md) for a reference output

---

### Step 5 — Automation Scaffold (Optional)

If the user requests Selenium/Playwright/Pytest scaffolding, generate a base test class using the pattern in [examples/automation-scaffold.md](examples/automation-scaffold.md).

---

## Resources

- [examples/login-test-cases.md](examples/login-test-cases.md) — Full test suite for OrangeHRM login page
- [examples/automation-scaffold.md](examples/automation-scaffold.md) — Pytest + Selenium scaffold
