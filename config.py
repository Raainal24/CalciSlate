"""
=========================================================
CalciSketch - Client Configuration
=========================================================

This file contains all project-wide settings, paths, and
constants used by the CalciSketch client application.
"""

from pathlib import Path

# =========================================================
# PROJECT DIRECTORIES
# =========================================================

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Assets
ASSETS_DIR = BASE_DIR / "Assets"

# Save files
SAVES_DIR = BASE_DIR / "Saves"

# Temporary screenshots
TEMP_DIR = BASE_DIR / "Temp"

# Log files
LOGS_DIR = BASE_DIR / "Logs"

# Backend package
BACKEND_DIR = BASE_DIR / "backend"

# =========================================================
# CREATE REQUIRED FOLDERS
# =========================================================

REQUIRED_FOLDERS = [
    SAVES_DIR,
    TEMP_DIR,
    LOGS_DIR
]

for folder in REQUIRED_FOLDERS:
    folder.mkdir(parents=True, exist_ok=True)

# =========================================================
# APPLICATION SETTINGS
# =========================================================

APP_NAME = "CalciSketch"

VERSION = "2.0"

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

MIN_WINDOW_WIDTH = 1280
MIN_WINDOW_HEIGHT = 720

# =========================================================
# DRAWING SETTINGS
# =========================================================

CANVAS_WIDTH = 1920
CANVAS_HEIGHT = 880

CANVAS_BACKGROUND = "white"

DEFAULT_BRUSH_COLOR = "black"

DEFAULT_BRUSH_SIZE = 3

MIN_BRUSH_SIZE = 1
MAX_BRUSH_SIZE = 10

ERASER_COLOR = "white"

# =========================================================
# HPC SERVER
# =========================================================

# Change this only if your FastAPI server address changes.

SERVER_URL = "http://localhost:8000"

SOLVE_ENDPOINT = f"{SERVER_URL}/solve"

REQUEST_TIMEOUT = 180

# =========================================================
# TEMP FILES
# =========================================================

SCREENSHOT_NAME = "equation.png"

SCREENSHOT_PATH = TEMP_DIR / SCREENSHOT_NAME

# =========================================================
# SAVE FILES
# =========================================================

SAVE_EXTENSION = ".pkl"

# =========================================================
# LOGGING
# =========================================================

LOG_FILE = LOGS_DIR / "calcisketch.log"

LOG_LEVEL = "INFO"

# =========================================================
# SUPPORTED IMAGE TYPES
# =========================================================

SUPPORTED_IMAGE_TYPES = [
    ".png",
    ".jpg",
    ".jpeg"
]

# =========================================================
# GUI ASSETS
# =========================================================

# Home Page
BACKGROUND_IMAGE = ASSETS_DIR / "bg img.png"
LOGO_IMAGE = ASSETS_DIR / "logo.png"

START_BUTTON_IMAGE = ASSETS_DIR / "START DRAWING.png"
ABOUT_BUTTON_IMAGE = ASSETS_DIR / "ABOUT US!!.png"

# Drawing Page
DRAWING_BACKGROUND = ASSETS_DIR / "image_1.png"

TOOLBAR_IMAGE = ASSETS_DIR / "button_1.png"

RED_BUTTON = ASSETS_DIR / "button_2.png"
YELLOW_BUTTON = ASSETS_DIR / "button_3.png"
GREEN_BUTTON = ASSETS_DIR / "button_4.png"
BLUE_BUTTON = ASSETS_DIR / "button_5.png"
WHITE_BUTTON = ASSETS_DIR / "button_6.png"
BLACK_BUTTON = ASSETS_DIR / "button_7.png"

ERASER_BUTTON = ASSETS_DIR / "button_8.png"
BRUSH_BUTTON = ASSETS_DIR / "button_9.png"

CALCULATE_BUTTON = ASSETS_DIR / "button_10.png"
CLEAR_BUTTON = ASSETS_DIR / "button_11.png"
SAVE_BUTTON = ASSETS_DIR / "button_12.png"
LOAD_BUTTON = ASSETS_DIR / "button_13.png"

# About Page
AMAL_CARD = ASSETS_DIR / "amal_Card.png"
SHIB_CARD = ASSETS_DIR / "shib_card.png"
DHARSHINI_CARD = ASSETS_DIR / "dharsh_Card.png"

# =========================================================
# END OF CONFIG
# =========================================================