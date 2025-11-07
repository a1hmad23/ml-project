"""
Features:
---------
1. Creates a `logs/` directory automatically (if it doesn't exist).
2. Generates a timestamped log file for each program run.
3. Logs messages both to a file (via basicConfig) and to the console (via StreamHandler).
4. Provides separate formatters for file and console output.
5. Uses the root logger for simplicity — meaning all `logging.info()`, `logging.error()`, etc.,
   will automatically write to both destinations.

Concepts:
---------
- **Root Logger**: The default logger used when you call logging.info(), etc.
- **Handlers**: Direct logs to destinations (file, console, etc.).
- **Formatters**: Control how log messages appear (timestamp, level, message).
- **Logging Levels**: DEBUG < INFO < WARNING < ERROR < CRITICAL
"""

from pathlib import Path
import logging
from datetime import datetime

# === 1. Define the log directory and ensure it exists ===
# Path.cwd() returns the current working directory.
# / "logs" appends the "logs" folder using Path's "/" operator.
# mkdir(parents=True, exist_ok=True) ensures the directory is created safely
log_dir = Path.cwd() / "logs"
log_dir.mkdir(parents=True, exist_ok=True)

# === 2. Create a timestamped log file ===
# This gives each program run a unique log file name.
# Example: "2025_11_05_17_35_22.log"
# datetime.now(): current date/time
# :%Y_%m_%d_%H_%M_%S → formatted timestamp
log_file = log_dir / f"{datetime.now():%Y_%m_%d_%H_%M_%S}.log"

# === 3. Configure the logging system (root logger) ===
# logging.basicConfig() sets up the root logger.
# When 'filename' is provided, it automatically creates a FileHandler that
# writes logs to the given file.
# The 'format' argument defines how each log line appears in the file.
# 'level=logging.INFO' means only INFO and higher levels will be recorded.
logging.basicConfig(
    filename=log_file,
    format="[%(asctime)s] %(levelname)s in %(name)s (line %(lineno)d): %(message)s",
    level=logging.INFO,
)

# === 4. Optional: also log to console (StreamHandler) ===
# By default, basicConfig() only logs to file here.
# To also see logs live in the terminal, we add a second handler (console).
console_handler = logging.StreamHandler()  # Output stream = sys.stderr by default
console_handler.setLevel(logging.INFO)     # Same level as the file handler

# Define a simpler format for console logs
# "%(asctime)s" = time of log
# "%(levelname)s" = severity (INFO, WARNING, etc.)
# "%(message)s" = log text
# Second argument "%H:%M:%S" formats time to only show hours, minutes, seconds.
console_formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s - %(message)s", "%H:%M:%S"
)
console_handler.setFormatter(console_formatter)

# Attach the console handler to the root logger.
# This creates a multi-handler setup:
# - FileHandler (created by basicConfig)
# - StreamHandler (added manually)
logging.getLogger().addHandler(console_handler)

# === 5. Example usage ===
# Any call to logging.info(), logging.warning(), etc., will now:
# - Write to the log file
# - Print to the console
# logging.info("Logging initialized successfully.")

