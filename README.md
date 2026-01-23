# BlazeDemo Automation Testing Project

## Project Description
This project contains automated UI tests for the BlazeDemo flight booking application. The tests cover flight search and booking functionality.

## Technologies Used
- Python
- Selenium WebDriver
- PyTest
- pytest-html

## Project Structure
```bash
asikk5/
├── tests/
│ └── test_blazedemo.py
├── screenshots/
├── reports/
├── logs/
├── utils/
├── conftest.py
└── README.md
```

## Prerequisites
- Python 3.9+
- Google Chrome browser
- ChromeDriver compatible with Chrome version

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/nurbibi10/testing.git
```
2. Navigate to project directory:
```bash
cd asikk5
```
3. Install dependencies:
- Selenium WebDriver
- PyTest

## Test Execution
Run all tests and generate HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

## Test Reports

HTML execution report is generated in the reports folder

Screenshots are saved in the screenshots folder on test failure

Logs are available in the logs folder
