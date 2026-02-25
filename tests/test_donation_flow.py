import pytest

BASE_URL = "https://data.fundraiseup.com/qa-test-7R58U3/"

@pytest.mark.smoke
def test_open_page_and_give_now(donation_page):
    donation_page.open(BASE_URL)

    donation_page.click_give_now()

@pytest.mark.e2e
def test_monthly_donation_flow(donation_page):
    donation_page.open(BASE_URL)
    donation_page.click_give_now()
    donation_page.switch_to_monthly()
    donation_page.donate_with_other_methods() 

    
