# OrangeHRM Login Test Suite

[![OrangeHRM Login Tests](https://github.com/Gayathriiyerblr/AntiGravity_Skills/actions/workflows/selenium-tests.yml/badge.svg)](https://github.com/Gayathriiyerblr/AntiGravity_Skills/actions/workflows/selenium-tests.yml)

Automated Pytest + Selenium test suite for the OrangeHRM login page.  
**URL:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

---

## 📁 Project Structure

```
AntiGravitySkills/
├── .github/
│   └── workflows/
│       └── selenium-tests.yml   # GitHub Actions CI/CD pipeline
├── .gitignore
├── tests/
│   └── orangehrm_login/
│       ├── conftest.py          # Chrome WebDriver fixture (auto-managed)
│       ├── pytest.ini           # Pytest config + HTML report settings
│       ├── requirements.txt     # Python dependencies
│       ├── pages/
│       │   ├── __init__.py
│       │   └── login_page.py    # Page Object Model
│       └── tests/
│           └── test_login.py    # 30 test cases (5 categories)
```

---

## ⚙️ Local Setup

### 1. Create a virtual environment (recommended)
```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```powershell
pip install -r requirements.txt
```

> ChromeDriver is managed automatically via `webdriver-manager`. No manual download needed.

---

## ▶️ Running Tests Locally

### Run all 30 tests
```powershell
pytest tests/ -v
```

### Run headless (no browser window)
```powershell
pytest tests/ -v --headless
```

### Run by category
```powershell
pytest tests/ -v -m positive      # ✅ Positive tests only
pytest tests/ -v -m negative      # ❌ Negative tests only
pytest tests/ -v -m boundary      # 🔢 Boundary tests only
pytest tests/ -v -m security      # 🔒 Security tests only
pytest tests/ -v -m ux            # 🎨 UX/UI tests only
```

### Run a specific test
```powershell
pytest tests/ -v -k "TC_LOGIN_001"
```

### Generate HTML report
```powershell
pytest tests/ -v --html=reports/report.html --self-contained-html
```

---

## 🚀 CI/CD — GitHub Actions

The pipeline is defined in [`.github/workflows/selenium-tests.yml`](../../.github/workflows/selenium-tests.yml).

### Triggers

| Event | When |
|---|---|
| **Push** | Any push to `main` or `master` touching test files |
| **Pull Request** | Any PR targeting `main` or `master` |
| **Manual** | Via GitHub UI → Actions → Run workflow (with optional category filter) |

### Pipeline Steps

```
Checkout → Setup Python → Install Chrome (Linux) → pip install → Run Tests (headless) → Upload HTML Report → Publish JUnit Summary
```

### Matrix Strategy

Runs on **both** `ubuntu-latest` and `windows-latest` in parallel.

### Artifacts

After each run, the HTML report is uploaded as a GitHub Actions artifact:

1. Go to **Actions** tab in your repo
2. Click the latest workflow run
3. Scroll to **Artifacts** → download `test-report-ubuntu-latest-py3.11`

### Manual Run with Category Filter

1. Go to **Actions** → **OrangeHRM Login Tests** → **Run workflow**
2. Select a category from the dropdown (or leave blank for all)
3. Click **Run workflow**

---

## 📊 Test Coverage

| Category    | Count | TC IDs               |
|---|---|---|
| ✅ Positive | 5     | TC-LOGIN-001 to 005  |
| ❌ Negative | 10    | TC-LOGIN-006 to 015  |
| 🔢 Boundary | 5     | TC-LOGIN-016 to 020  |
| 🔒 Security | 5+    | TC-LOGIN-021 to 025  |
| 🎨 UX / UI  | 5     | TC-LOGIN-026 to 030  |

> Security tests are parametrized and expand to ~10 actual test runs.

---

## 🔑 Test Credentials

| Field    | Value      |
|---|---|
| Username | `Admin`    |
| Password | `admin123` |

> The OrangeHRM demo resets periodically. Verify credentials are still valid before running.

---

## 🛠️ Push to GitHub

```powershell
# Initialise git (if not already done)
git init
git add .
git commit -m "feat: add OrangeHRM login test suite with GitHub Actions CI/CD"

# Add your remote and push
git remote add origin https://github.com/Gayathriiyerblr/AntiGravity_Skills.git
git branch -M main
git push -u origin main
```

Once pushed, GitHub Actions will automatically trigger and run your tests on every commit.
