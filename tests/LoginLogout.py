import unittest
import time
from selenium import webdriver


class Shadyoaks_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")

        time.sleep(3)
        print("Opening Shady Oaks Home Page")
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

        time.sleep(5)

        header = driver.find_element_by_css_selector("#myHeader > div > h1")

        if header.is_displayed():
            print("Reached Home page with successful login!")

        else:
            print("Login Failed. Try Again.")

        #logout functionality

        logout_button = driver.find_element_by_css_selector("#myHeader > span > p > a")

        logout_button.click()
        print("Clicked logout button")

        time.sleep(5)

        logout_header = driver.find_element_by_css_selector("body > div > h2")

        if logout_header.is_displayed():
            print("Reached Logout page successfully!")

        else:
            print("Logout Failed.")

    def tearDown(self):
        self.driver.close()

