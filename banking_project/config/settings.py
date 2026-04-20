from pathlib import Path

# ===============================
# Base directory
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# Logging configuration
# ===============================
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"

LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
