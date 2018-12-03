import unittest
import time
from selenium import webdriver


class Tee_Test1_upwd(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_admin(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        username_text_field = driver.find_element_by_id("id_username")
        username_text_field.send_keys(user)
        password_text_field = driver.find_element_by_id("id_password")
        password_text_field.send_keys(pwd)
        button = driver.find_element_by_css_selector("input[type='submit']")
        button.click()
        time.sleep(5)
        driver.find_element_by_link_text("Django administration")

    def tearDown(self):
        self.driver.close()