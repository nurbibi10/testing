import pytest
import os
from datetime import datetime
from selenium import webdriver
from utils.logger import logger


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"{screenshots_dir}/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)
            logger.error(f"Test failed. Screenshot saved: {screenshot_path}")

            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.image(screenshot_path))
