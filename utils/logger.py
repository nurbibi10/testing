import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger()
