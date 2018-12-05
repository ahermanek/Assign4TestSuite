import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()
        elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[4]").click()
        elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()

        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/")
        assert "Logged In"
        time.sleep(2)

        elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()
        elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[4]").click()
        elem = driver.find_element_by_xpath("//*[@id='myHeader']/span/i").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='mySidebar']/a[5]").click()

        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_xpath("//*[@id='user-tools']/a[3]").click()

        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

