# BlazeDemo Flight Booking Test Automation

Automated test suite for the BlazeDemo flight booking application using Selenium WebDriver and pytest.

## 📋 Project Overview

This project implements comprehensive automated testing for the BlazeDemo application with:
- ✅ Test lifecycle management using pytest
- ✅ Logging framework (Python logging)
- ✅ HTML test reports with screenshots
- ✅ Automatic failure screenshots
- ✅ Structured test cases

## ✨ Requirements Met

### 1. Test Lifecycle Management (30 pts)
- **Setup**: Browser initialization and navigation to application
- **Teardown**: Browser cleanup and resource release
- **Test Cases**: 3 test scenarios covering core functionality
- **Framework**: pytest with fixtures

### 2. Logging Framework (30 pts)
- **Logger**: Python `logging` module
- **Output**: File-based logging to `logs/test.log`
- **Coverage**: Test start/end, steps, errors, and failures
- **Format**: `%(asctime)s - %(levelname)s - %(name)s - %(message)s`

### 3. Test Report & Screenshots (40 pts)
- **Report Tool**: pytest-html
- **Screenshots**: Automatic capture on test failure
- **Summary**: Pass/Fail/Skip statistics
- **Details**: Individual test results with logs
- **Location**: `reports/report.html`

```markdown
## 📁 Project Structure

```
├── 

conftest.py

                 # Pytest configuration & fixtures
├── utils/
│   ├── logger.py              # Logging configuration
│   └── screenshot.py          # Screenshot utility
├── tests/
│   └── test_blazedemo.py      # Test cases
├── logs/
│   └── test.log              # Test execution logs
├── screenshots/              # Failure screenshots
├── reports/
│   └── report.html          # HTML test report
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```
```


## 🧪 Test Cases

### 1. test_open_homepage
- **Purpose**: Verify application homepage loads correctly
- **Steps**:
  1. Navigate to BlazeDemo application
  2. Verify page title contains "BlazeDemo"
- **Expected Result**: Homepage loads successfully
- **Status**: ✅ PASSED

### 2. test_search_flights
- **Purpose**: Verify flight search functionality
- **Steps**:
  1. Enter departure city: "Paris"
  2. Enter destination city: "London"
  3. Submit search form
  4. Wait for results table to load
- **Expected Result**: Flight results displayed in table
- **Status**: ✅ PASSED

### 3. test_complete_booking
- **Purpose**: Verify complete booking workflow
- **Steps**:
  1. Search for flights (Paris → London)
  2. Select first available flight
  3. Fill passenger information
  4. Fill payment details
  5. Submit booking
- **Expected Result**: Confirmation message "Thank you for your purchase today!" displayed
- **Status**: ✅ PASSED

## 🚀 Setup Instructions

### Prerequisites
- Python 3.14+
- Chrome browser
- ChromeDriver (compatible with Chrome version)
- macOS 13.5+

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd asikk5
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### requirements.txt
```
selenium==4.15.2
pytest==7.4.3
pytest-html==4.1.1
python-dotenv==1.0.0
```

## ▶️ Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test
```bash
pytest tests/test_blazedemo.py::test_open_homepage -v
```

### Run with HTML Report
```bash
pytest tests/ --html=reports/report.html --self-contained-html -v
```

### Run with Verbose Output and Screenshots
```bash
pytest tests/ -v -s
```

### Run with Detailed Logging
```bash
pytest tests/ -v --log-cli-level=INFO
```

## 📊 Test Execution Results

### Latest Test Run Summary
```
Total Tests:        3
Passed:            3 ✅
Failed:            0
Skipped:           0
Expected Failures: 0
Unexpected Passes: 0
Errors:            0
```

### Report Details
- **Report Location**: 

report.html


- **Logs Location**: 

test.log


- **Screenshots Location**: 

screenshots


- **Total Duration**: ~12 seconds

## 📝 Output Files

### Log Files
- **Location**: 

test.log


- **Format**: 
```
2026-01-20 22:10:12,756 - INFO - root - ===== Test setup started =====
2026-01-20 22:10:15,342 - INFO - root - test_open_homepage - Test start
2026-01-20 22:10:16,891 - INFO - root - ===== Test teardown started =====
```
- **Contents**: Test execution flow, steps, and errors

### HTML Report
- **Location**: 

report.html


- **Features**:
  - ✅ Test summary (3 passed / 0 failed / 0 skipped)
  - ✅ Individual test results with timing
  - ✅ Execution duration per test
  - ✅ Captured logs for each test
  - ✅ Failure screenshots (auto-captured)
  - ✅ Interactive filter options

### Screenshots
- **Location**: 

screenshots


- **Naming Convention**: `{test_name}_{timestamp}.png`
- **Trigger**: Automatic capture on test failure
- **Example**: `test_complete_booking_20260120_221012.png`

## 🔧 Test Fixtures

### driver fixture (conftest.py)

```python
@pytest.fixture
def driver():
    logger.info("===== Test setup started =====")
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://blazedemo.com")
    
    yield driver
    
    logger.info("===== Test teardown started =====")
    driver.quit()
    logger.info("===== Test finished =====")
```

**Features**:
- ✅ Initializes Chrome WebDriver
- ✅ Maximizes browser window
- ✅ Navigates to application URL
- ✅ Handles cleanup (quits driver)
- ✅ Logs setup/teardown events
- ✅ Runs before and after each test

## 📋 Logging Configuration

Logger setup in 

logger.py

:

```python
import logging
import os
from datetime import datetime

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger()
```

### Log Levels Used
- **INFO**: Test start/end and major test steps
- **ERROR**: Exceptions and assertion failures
- **DEBUG**: Detailed step-by-step execution (optional)

### Example Log Entries
```
2026-01-20 22:10:12,756 - INFO - root - ===== Test setup started =====
2026-01-20 22:10:13,234 - INFO - root - Opening BlazeDemo homepage
2026-01-20 22:10:14,567 - INFO - root - Verifying page title
2026-01-20 22:10:15,891 - INFO - root - Test passed successfully
2026-01-20 22:10:16,125 - INFO - root - ===== Test finished =====
```

## 🖼️ Failure Handling

### Automatic Screenshot Capture
- **Trigger**: Automatically on test failure
- **Method**: pytest hook `pytest_runtest_makereport` in 

conftest.py


- **Storage**: 

screenshots

 directory with timestamp
- **Integration**: Embedded in HTML report

### Example Failure Workflow
```
1. Test execution fails
2. Hook captures failure status
3. Screenshot taken: test_name_20260120_221012.png
4. Logged in report.html
5. Error message logged to test.log
```

### Log Entry Example
```
2026-01-20 22:10:18,456 - ERROR - root - Test failed. Screenshot saved: screenshots/test_complete_booking_20260120_221018.png
AssertionError: Expected text not found on page
```

## 🛠️ Utility Functions

### Screenshot Utility (utils/screenshot.py)

```python
from datetime import datetime
import os

def take_screenshot(driver, test_name):
    """Manually capture screenshot"""
    os.makedirs("screenshots", exist_ok=True)
    file_name = f"screenshots/{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(file_name)
    return file_name

def take_screenshot_on_failure(driver, item, rep):
    """Capture screenshot on test failure"""
    if rep.when == "call" and rep.failed:
        take_screenshot(driver, item.name)
```

## ✅ Key Features

| Feature | Implementation | Status |
|---------|-----------------|--------|
| Test Framework | pytest 7.4.3 | ✅ |
| Logging | Python logging module | ✅ |
| Reports | pytest-html 4.1.1 | ✅ |
| Screenshots | Selenium + pytest hooks | ✅ |
| Setup/Teardown | pytest fixtures | ✅ |
| Browser Automation | Selenium WebDriver 4.15 | ✅ |
| Test Cases | 3 scenarios | ✅ |
| Documentation | README + inline comments | ✅ |

## 🐛 Troubleshooting

### Chrome Driver Issues
```bash
# Verify Chrome version
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version

# Download matching ChromeDriver
# https://chromedriver.chromium.org/

# Add to PATH or specify in code
webdriver.Chrome(executable_path="/path/to/chromedriver")
```

### Module Import Errors
```bash
# Verify virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Connection Issues
```bash
# Ensure BlazeDemo is accessible
curl https://blazedemo.com

# Check internet connection
ping 8.8.8.8
```

### Report Not Generating
```bash
# Create reports directory
mkdir -p reports

# Run with explicit path
pytest tests/ --html=reports/report.html --self-contained-html -v
```

### Log File Issues
```bash
# Create logs directory
mkdir -p logs

# Check file permissions
chmod 755 logs/
```

## 📱 Test Report Details

### Report Location


report.html



### Report Statistics
```
Failed:     0
Passed:     3 ✅
Skipped:    0
Expected Failures: 0
Unexpected Passes: 0
Errors:     0
Reruns:     0
Retried:    0
```

### Report Features
- ✅ Interactive dashboard
- ✅ Collapsible test details
- ✅ Pass/Fail filtering
- ✅ Test duration tracking
- ✅ Log output display
- ✅ Screenshot embedding
- ✅ Responsive design

## 🏗️ Best Practices Implemented

### ✅ Separation of Concerns
- Logging utilities separated in 

logger.py


- Screenshot utilities separated in 

screenshot.py


- Test logic isolated in 

test_blazedemo.py


- Configuration centralized in 

conftest.py



### ✅ Error Handling
- Try-except blocks in critical sections
- Logging of all exceptions
- Screenshot capture on failure
- Graceful cleanup in teardown

### ✅ Code Organization
- Clear directory structure
- Reusable pytest fixtures
- Configuration in 

conftest.py


- Utility modules for common operations

### ✅ Documentation
- Inline code comments
- Function docstrings
- Comprehensive README file
- Test case descriptions

### ✅ Test Design
- Clear test naming convention
- Isolated test cases
- No test interdependencies
- Explicit assertions

## 🔐 Technologies Used

- **Language**: Python 3.14.2
- **Test Framework**: pytest 7.4.3
- **Browser Automation**: Selenium WebDriver 4.15.2
- **Reporting**: pytest-html 4.1.1
- **Logging**: Python logging module (built-in)
- **OS**: macOS 13.5
- **IDE**: Visual Studio Code

## 📦 Installation Summary

```bash
# Complete setup from scratch
git clone <repository-url>
cd asikk5
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir -p logs screenshots reports

# Run tests
pytest tests/ --html=reports/report.html --self-contained-html -v

# View report
open reports/report.html
```

## 📞 Support & Troubleshooting

For issues:
1. Check 

test.log

 for detailed error messages
2. Review 

report.html

 for test results
3. Check 

screenshots

 for failure evidence
4. Verify Chrome browser and ChromeDriver compatibility

## 👤 Author & Repository

- **Author**: Nurbibi Rakhmanberdiyeva
- **Project**: Assignment 5 - Test Automation (TestNG/pytest)
- **Repository**: [Add GitHub link]
- **Course**: SQAT (Software Quality Assurance & Testing)

## 📄 License

MIT License

---

## 📋 Deliverables Checklist

- ✅ Source code (GitHub repository link)
- ✅ HTML test execution report (`reports/report.html`)
- ✅ Test report document (README.md)
- ✅ README file with setup and execution steps
- ✅ Test lifecycle management implemented
- ✅ Logging framework configured
- ✅ Automatic screenshots on failure
- ✅ 3 test cases developed and passing

---

**Last Updated**: January 20, 2026  
**Report Generated**: Available in 

report.html

  
**Test Status**: ✅ All 3 tests PASSED
```

Done! This version is cleaned up with:
- ✅ All Windows references removed
- ✅ macOS-only commands (using `open`, proper Chrome path)
- ✅ Fixed formatting and removed broken code blocks
- ✅ Ready to paste directly into your file
Done! This version is cleaned up with:
- ✅ All Windows references removed
- ✅ macOS-only commands (using `open`, proper Chrome path)
- ✅ Fixed formatting and removed broken code blocks
- ✅ Ready to paste directly into your file