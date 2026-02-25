import pytest
from playwright.sync_api import sync_playwright
from pages.donation_page import DonationPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def donation_page(page):
    return DonationPage(page)