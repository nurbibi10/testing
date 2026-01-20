from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


def test_open_homepage(driver):
    logger.info("Start test: Open homepage")

    try:
        assert "BlazeDemo" in driver.title
        logger.info("Homepage opened successfully")

    except Exception:
        logger.exception("Error in test_open_homepage")
        raise


def test_search_flights(driver):
    logger.info("Start test: Search flights")

    try:
        driver.find_element(By.NAME, "fromPort").send_keys("Paris")
        driver.find_element(By.NAME, "toPort").send_keys("London")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        logger.info("Flight search submitted")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        logger.info("Flights table loaded successfully")

    except Exception:
        logger.exception("Error in test_search_flights")
        raise


def test_complete_booking(driver):
    logger.info("Start test: Complete booking")

    try:
        driver.find_element(By.NAME, "fromPort").send_keys("Paris")
        driver.find_element(By.NAME, "toPort").send_keys("London")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        logger.info("Flights search submitted")

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Choose This Flight']"))
         ).click()

        logger.info("Flight selected")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inputName"))
        )

        driver.find_element(By.ID, "inputName").send_keys("Test User")
        driver.find_element(By.ID, "address").send_keys("Test Address")
        driver.find_element(By.ID, "city").send_keys("Almaty")
        driver.find_element(By.ID, "state").send_keys("KZ")
        driver.find_element(By.ID, "zipCode").send_keys("050000")
        driver.find_element(By.ID, "creditCardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "nameOnCard").send_keys("Test User")

        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        confirmation_text = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text

        assert confirmation_text == "Thank you for your purchase today!"
        logger.info("Booking completed successfully")


    except Exception:
        logger.exception("Error in test_complete_booking")
        raise
