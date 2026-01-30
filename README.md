# Full-Stack Test Automation Framework

Selenium + Pytest automation framework for testing vendor panel signup/login flows.

## Quick Start

### 1. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Configure Environment
Edit `.env` file with your settings:
```env
BASE_URL=https://dev.v.shipgl.in
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_DATABASE=staging
HEADLESS=false  # false=UI mode (see browser), true=CI/CD mode
```

### 3. Run Tests

**UI Mode (see browser):**
```bash
HEADLESS=false ./venv/bin/pytest tests/authentication -v
```

**CI/CD Mode (headless/background):**
```bash
HEADLESS=true ./venv/bin/pytest tests/authentication -v
```

**Or use venv directly:**
```bash
source venv/bin/activate
pytest tests/authentication -v
```

## Test Structure

- **test_01_auth_e2e.py** - Complete signup → login flow
- **test_02_signup_positive.py** - Valid signup test
- **test_03_signup_negative.py** - 19 validation test cases (invalid data)
- **test_04_login_positive.py** - Valid login test
- **test_05_login_negative.py** - 8 validation test cases (invalid credentials)

## Project Structure

```
src/
  ├─ core/base_page.py          # Base page object class
  ├─ pages/                      # Page object models
  ├─ flows/                      # Multi-step test flows
  ├─ locators/                   # CSS/XPath selectors
  └─ utils/                      # Database, session helpers

tests/
  └─ authentication/             # Auth test cases

.env                             # Configuration (DO NOT COMMIT passwords)
pytest.ini                       # Pytest settings
requirements.txt                 # Python dependencies
```

## Performance

- **30 tests** run in ~2 minutes (optimized)
- Signup negative: 19 cases on ONE page load + refresh
- Login negative: 8 cases on ONE page load + refresh
- No browser reopening between test cases = FAST ⚡

## Features

✅ Headless + UI mode support  
✅ Environment-based configuration (.env)  
✅ MySQL database integration  
✅ Page Object Model pattern  
✅ Optimized with page refresh (no reopening)

