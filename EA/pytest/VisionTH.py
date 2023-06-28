# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestVisionTH():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_visionTH(self):
    # Test name: Vision TH
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get("http://192.168.241.210/")
    # 2 | setWindowSize | 1936x1056 |  | 
    self.driver.set_window_size(1936, 1056)
    # 3 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    # 4 | click | css=.fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    # 5 | click | linkText=TH |  | 
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    # 6 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    # 7 | click | css=.fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    # 8 | click | css=.line-hover:nth-child(2) .triangle |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".line-hover:nth-child(2) .triangle").click()
    # 9 | click | linkText=วิสัยทัศน์และพันธกิจ |  | 
    self.driver.find_element(By.LINK_TEXT, "วิสัยทัศน์และพันธกิจ").click()
  