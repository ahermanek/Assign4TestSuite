import unittest
import time
from selenium import webdriver


class Shadyoaks_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_pages(self):
        driver = self.driver
        driver.maximize_window()
        print("Opening Shady Oaks Home Page")

        #If new pythonanywhere site is used, update this hard-coded value.
        driver.get("http://127.0.0.1:8000")
        print("Got to Home Page")

        #first page objects
        login_button = driver.find_element_by_css_selector("#myHeader > span > p > a")

        login_button.click()
        print("Log in button clicked")

        #second page objects
        username_button = driver.find_element_by_css_selector("#id_username")
        password_button = driver.find_element_by_css_selector("#id_password")
        submit_button = driver.find_element_by_css_selector("body > div > form > input[type='submit']:nth-child(9)")

        username_button.send_keys("instructor")
        print("username input entered")

        password_button.send_keys("instructor1a")
        print("password input entered")

        submit_button.click()
        print("Submit button clicked")

        driver.implicitly_wait(30)

        header = driver.find_element_by_css_selector("body > div.page-container > h2")

        if header.is_displayed():
            print("Reached Home page with successful login!")
        else:
            print("Login Failed. Try Again.")

        navigation_tab = driver.find_element_by_css_selector("#myHeader > span > i")
        navigation_tab.click()

        nav_memberships = driver.find_element_by_css_selector("#mySidebar > a:nth-child(2)")
        nav_memberships.click()
        driver.implicitly_wait(200)

        membership_title = driver.find_element_by_css_selector("#member > h1")
        driver.implicitly_wait(200)

        if membership_title.is_displayed():
            print("Reached the Membership Page!")

        else:
            print("Page Not Reached!")

        navigation_tab = driver.find_element_by_css_selector("#myHeader > span > i")
        navigation_tab.click()

        nav_scheduling = driver.find_element_by_css_selector("#mySidebar > a:nth-child(3)")
        nav_scheduling.click()

        driver.implicitly_wait(200)

        schedule_title = driver.find_element_by_css_selector("#myHeader > div > h1")

        if schedule_title.is_displayed():
            print("Reached the Scheduler Page!")

        else:
            print("Page Not Reached!")

        navigation_tab = driver.find_element_by_css_selector("#myHeader > span > i")
        navigation_tab.click()
        nav_events = driver.find_element_by_css_selector("#mySidebar > a:nth-child(4)")
        nav_events.click()

        driver.implicitly_wait(90)

        events_title = driver.find_element_by_css_selector("#myHeader > div > h1")

        if events_title.is_displayed():
            print("Reached Events Page!")
        else:
            print("Page not Reached!")

        navigation_tab = driver.find_element_by_css_selector("#myHeader > span > i")
        navigation_tab.click()
        nav_contact = driver.find_element_by_css_selector("#mySidebar > a:nth-child(5)")
        nav_contact.click()

        driver.implicitly_wait(90)

        contact_title = driver.find_element_by_css_selector("body > div:nth-child(3) > div:nth-child(1) > h1")

        if contact_title.is_displayed():
            print("Contact Page Reached!")
        else:
            print("Page not Reached!")

        driver.implicitly_wait(90)

        navigation_tab = driver.find_element_by_css_selector("#myHeader > span > i")
        navigation_tab.click()
        nav_close = driver.find_element_by_css_selector("#mySidebar > button")
        nav_close.click()

        driver.implicitly_wait(90)

        if contact_title.is_displayed():
            print("Close button functionality successful!")
            print("Test Case Successful!")
        else:
            print("Error!")
            print("Test Cases unsuccessful!")

    def tearDown(self):
        self.driver.close()
