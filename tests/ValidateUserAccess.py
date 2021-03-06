import unittest
import time
from selenium import webdriver


class Shadyoaks_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_buttons(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")

        navigation_tab = driver.find_element_by_css_selector("#myHeader > span > i")
        navigation_tab.click()

        nav_scheduling = driver.find_element_by_css_selector("#mySidebar > a:nth-child(3)")
        nav_scheduling.click()

        accessPrompt = driver.find_element_by_css_selector("body > div > div")

        if accessPrompt.is_displayed():
            print("user not logged in, proper message Displayed!")
        else:
            print("Access Error!")

        driver.get("http://127.0.0.1:8000/")

        time.sleep(3)
        print("Opening Shady Oaks Home Page")
        print("Got to Home Page")

        # first page objects
        login_button = driver.find_element_by_css_selector("#myHeader > span > p > a")

        login_button.click()
        print("Log in button clicked")

        # second page objects
        username_button = driver.find_element_by_css_selector("#id_username")
        password_button = driver.find_element_by_css_selector("#id_password")
        submit_button = driver.find_element_by_css_selector("body > div > form > input[type='submit']:nth-child(9)")

        username_button.send_keys("instructor")
        print("username input entered")

        password_button.send_keys("instructor1a")
        print("password input entered")

        submit_button.click()
        print("Submit button clicked")

        navigation_tab = driver.find_element_by_css_selector("#myHeader > span > i")
        navigation_tab.click()

        nav_scheduling = driver.find_element_by_css_selector("#mySidebar > a:nth-child(3)")
        nav_scheduling.click()

        teeTimeTable = driver.find_element_by_css_selector("body > div > table > thead > tr")

        if teeTimeTable.is_displayed():
            print("user logged in, table displayed!")
        else:
            print("Table not visible. Error!")

        def tearDown(self):
            self.driver.close()