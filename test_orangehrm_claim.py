# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestClaimSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_claim_search(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR,".oxd-form").submit()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[11]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/claim/viewAssignClaim")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/form/div/div/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/form/div/div/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/form/div/div/div/div/div[2]/div/div/input").send_keys("Odis")
        time.sleep(10)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/claim/assignClaim/id/7")

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
