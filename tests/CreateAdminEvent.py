import unittest
import time
from selenium import webdriver


class TestCreateAdminEvent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_events(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")

        time.sleep(3)

        username_button = driver.find_element_by_css_selector("#id_username")
        password_button = driver.find_element_by_css_selector("#id_password")
        submit_button = driver.find_element_by_css_selector("#login-form > div.submit-row > input[type='submit']")

        username_button.send_keys("instructor")
        print("username input entered")

        password_button.send_keys("instructor1a")
        print("password input entered")

        submit_button.click()
        print("Submit button clicked")

        time.sleep(5)

        header = driver.find_element_by_css_selector("#site-name > a")

        if header.is_displayed():
            print("Reached Admin Home page with successful login!")

        else:
            print("Login Failed. Try Again.")
            driver.close()

        clickAddEvent = driver.find_element_by_css_selector("#content-main > div.app-main.module > table > tbody > tr > td:nth-child(2) > a")
        clickAddEvent.click()

        #add event data

        eventName = driver.find_element_by_css_selector("#id_event_name")
        eventName.send_keys("Automation Test Event")

        attendess = driver.find_element_by_css_selector("#id_attendees")
        attendess.send_keys("250")

        organization = driver.find_element_by_css_selector("#id_organization")
        organization.send_keys("UNO")

        contact = driver.find_element_by_css_selector("#id_contact_number")
        contact.send_keys("402-111-1111")

        saveButton= driver.find_element_by_css_selector("#event_form > div > div > input.default")
        saveButton.click()

        #Viewing the updates
        viewsite = driver.find_element_by_css_selector("#user-tools > a:nth-child(2)")
        viewsite.click()

        hamburgerButton =driver.find_element_by_css_selector("#myHeader > span > i")
        hamburgerButton.click()

        eventsButton = driver.find_element_by_css_selector("#mySidebar > a:nth-child(4)")
        eventsButton.click()

        eventPresent = driver.find_element_by_css_selector("body > div.row > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(1)")

        if eventPresent.is_displayed():
            print("Event Saved and Seen was successful!")

        else:
            print("Login Failed. Try Again.")
            driver.close()

        driver.get("http://127.0.0.1:8000/admin")

        eventsTab = driver.find_element_by_css_selector("#content-main > div.app-main.module > table > tbody > tr > th > a")
        eventsTab.click()

        newEvent = driver.find_element_by_css_selector("#result_list > tbody > tr:nth-child(1) > th > a")
        newEvent.click()

        deleteEvent = driver.find_element_by_css_selector("#event_form > div > div > p > a")
        deleteEvent.click()

        verifydelete = driver.find_element_by_css_selector("#content > form > div > input[type='submit']:nth-child(2)")
        verifydelete.click()

    def tearDown(self):
        print("Driver Closed!")
        self.driver.close()
