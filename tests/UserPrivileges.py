import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ShadyOaksTestUserPrivileges(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_user(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(5)
        elem = driver.find_element_by_css_selector("#content-main > div.app-auth.module > "
                                                   "table > tbody > tr.model-user > th > a").click()
        time.sleep(5)
        elem = driver.find_element_by_css_selector("#content-main > ul > li > a").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("tester")
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys("maverick1a")
        time.sleep(5)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("maverick1a")
        time.sleep(5)
        elem = driver.find_element_by_css_selector("#user_form > div > div > input.default").click()
        time.sleep(5)

        logout = driver.find_element_by_css_selector("#user-tools > a:nth-child(4)").click()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("tester")
        time.sleep(5)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick1a")
        time.sleep(5)
        submit = driver.find_element_by_css_selector("#login-form > div.submit-row > input[type='submit']")
        submit.click()
        time.sleep(5)
        message = driver.find_element_by_css_selector("#content > p")

        time.sleep(5)
        if message.is_displayed():
            print("User not granted access!")
        else:
            print("Error! Not running as functioned.")
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(5)
        elem = driver.find_element_by_css_selector("#content-main > div.app-auth.module > "
                                                   "table > tbody > tr.model-user > th > a").click()
        search = driver.find_element_by_css_selector("#searchbar")
        search.send_keys("tester")
        submitsearch = driver.find_element_by_css_selector("#changelist-search > div > "
                                                           "input[type='submit']:nth-child(3)")
        submitsearch.click()
        selectItem = driver.find_element_by_css_selector("#result_list > tbody > tr:nth-child(1) > th > a").click()
        delete = driver.find_element_by_css_selector("#user_form > div > div > p > a").click()
        finalDelete = driver.find_element_by_css_selector("#content > form > div > "
                                                          "input[type='submit']:nth-child(2)").click()

    def tearDown(self):
        self.driver.close()