import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import csv

class Tee_Test_addGroup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_user(self):
        # Repeat from scratch logging in
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/admin')
        username_text_field = driver.find_element_by_id("id_username")
        username_text_field.send_keys(user)
        password_text_field = driver.find_element_by_id("id_password")
        password_text_field.send_keys(pwd)
        button = driver.find_element_by_css_selector("input[type='submit']")
        button.click()
        time.sleep(5)
        # Begin add group part of test
        driver.get('http://127.0.0.1:8000/admin/auth/group/add/')
        vtext_field = driver.find_element_by_id("id_name")
        vtext_field.send_keys("GroupTest")

        #Save
        button = driver.find_element_by_name("_save")
        button.click()
        time.sleep(5)

        #Delete
        driver.find_element_by_link_text("GroupTest").click()
        time.sleep(5)
        button = driver.find_element_by_class_name("deletelink")
        button.click()
        time.sleep(5)
        #Yes really really Delete
        button = driver.find_element_by_css_selector("input[type='submit']")
        button.click()

    def tearDown(self):
        self.driver.close()
