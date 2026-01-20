import os
from datetime import datetime

def take_screenshot(driver, test_name):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    file_name = f"screenshots/{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(file_name)
