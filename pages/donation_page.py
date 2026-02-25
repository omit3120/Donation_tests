from playwright.sync_api import Page, expect
from pages.base_page import base_page

class DonationPage(base_page):

    # Локаторы
    GIVE_NOW_BTN_IFRAME = "iframe[title='Donate Button']"
    SECURE_FORM = "iframe[title='Donation Form']"
    MONTHLY_TAB = "text=Monthly"
    DONATE_OTHER_BTN = "text=Donate with other methods"

    ENTER_YOUR_DETAILS_FORM = "#screen-header-:r8v:"

    
    
    SUBMIT_BUTTON = "button[type='submit']"

    def click_give_now(self):
        frame = self.page.frame_locator(self.GIVE_NOW_BTN_IFRAME)
        

        give_btn = frame.locator("[data-testid='donate-button']")
        expect(give_btn).to_be_visible(timeout=20000)
    
        give_btn.click()
        self.page.wait_for_url("**/qa-test-7R58U3/**", timeout=30000)

    def switch_to_monthly(self):
        form_frame = self.page.frame_locator("iframe[title='Donation Form']")
        secure_form_check = form_frame.locator("[data-testid='checkout-wrapper-modal']")
        expect(secure_form_check).to_be_visible(timeout=20000)
        monthly_tab_check = form_frame.locator("[data-qa='more-frequent-button']")
        expect(monthly_tab_check).to_be_visible(timeout = 10000)
        


    def donate_with_other_methods(self):
        form_frame = self.page.frame_locator("iframe[title='Donation Form']")
        other_btn = form_frame.locator("[data-qa='donate-with-other-methods-button']")
        expect(other_btn).to_be_visible(timeout=10000)
        other_btn.click()
        expect(form_frame.locator("[data-qa='personal-first-name']")).to_be_visible()            
        expect(form_frame.locator("[data-qa='personal-last-name']")).to_be_visible()
        expect(form_frame.locator("[data-qa='personal-email']")).to_be_visible()
        expect(form_frame.locator("[data-qa='privacy-continue']")).to_be_visible()
        expect(form_frame.locator("[data-qa='privacy-continue']")).to_be_enabled()


    #def verify_enter_details_fields_visible(self):
        #form_frame = self.page.frame_locator("iframe[title='Donation Form']")
        

        