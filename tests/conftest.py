"""
Pytest configuration for authentication tests
Handles browser session management and test setup/teardown
Supports LOCAL (UI mode) and CI/CD (headless mode) execution

Correct SeleniumBase usage:
  - Headless controlled via --headless flag (pytest CLI)
  - Environment variable (HEADLESS) adds --headless automatically
  - No manual webdriver configuration needed
"""
import pytest
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read configuration directly from .env
BASE_URL = os.getenv("BASE_URL", "https://dev.v.shipgl.in")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


def pytest_configure(config):
    """
    Configure pytest with SeleniumBase options based on HEADLESS env var.
    This runs before tests start.
    
    If HEADLESS=true in .env -> automatically adds --headless flag
    If HEADLESS=false in .env -> runs with normal browser (UI mode)
    """
    # Check if --headless is already set via CLI
    if not any(arg.startswith('--headless') for arg in config.invocation_params.args):
        # Add headless flag if HEADLESS=true in .env
        if HEADLESS:
            # Use pytest's internal API to set option
            config.option.headless = True
            print(f"\n{'='*70}")
            print(f"🤖 CI/CD MODE - HEADLESS BROWSER")
            print(f"   Browser: {BROWSER} (headless)")
            print(f"   Base URL: {BASE_URL}")
            print(f"   No GUI - Running in background")
            print(f"{'='*70}\n")
        else:
            config.option.headless = False
            print(f"\n{'='*70}")
            print(f"👀 LOCAL MODE - BROWSER VISIBLE")
            print(f"   Browser: {BROWSER}")
            print(f"   Base URL: {BASE_URL}")
            print(f"   You WILL see the browser window")
            print(f"{'='*70}\n")

