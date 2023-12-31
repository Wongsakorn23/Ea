# Generated by Selenium IDE
import pytest
import time
import json
import allure
from SC import take_screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestREADY100():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://192.168.41.66:4445', desired_capabilities=DesiredCapabilities.CHROME)
    #self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_1(self):
    try:
      self.driver.get("https://demo.irplus.in.th/Listed/SUSCO/homepage.asp")
      #self.driver.set_window_size(1936, 1056)
      time.sleep(2)
      self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
      self.driver.find_element(By.LINK_TEXT, "TH").click()
      time.sleep(2)
      self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
      # WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "หน้าหลัก")))
      # self.driver.find_element(By.LINK_TEXT, "หน้าหลัก").click()
      # time.sleep(2)
      # self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
      self.driver.find_element(By.LINK_TEXT, "ยอมรับ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".parallax")))
      elements = self.driver.find_elements(By.CSS_SELECTOR, ".parallax")
      assert len(elements) > 0
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "สารจากประธานกรรมการ")))
      self.driver.find_element(By.LINK_TEXT, "สารจากประธานกรรมการ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "สารจากประธานกรรมการ"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ความเป็นมา")))
      self.driver.find_element(By.LINK_TEXT, "ความเป็นมา").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ความเป็นมา"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "วิสัยทัศน์ / พันธกิจ")))
      self.driver.find_element(By.LINK_TEXT, "วิสัยทัศน์ / พันธกิจ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "วิสัยทัศน์ / พันธกิจ"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "โครงสร้างธุรกิจ")))
      self.driver.find_element(By.LINK_TEXT, "โครงสร้างธุรกิจ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "โครงสร้างธุรกิจ"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "คณะกรรมการบริษัท")))
      self.driver.find_element(By.LINK_TEXT, "คณะกรรมการบริษัท").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "คณะกรรมการบริษัท"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "คณะผู้บริหาร")))
      self.driver.find_element(By.LINK_TEXT, "คณะผู้บริหาร").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "คณะผู้บริหาร"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "โครงสร้างการจัดการ")))
      self.driver.find_element(By.LINK_TEXT, "โครงสร้างการจัดการ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "โครงสร้างการจัดการ"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ความรับผิดชอบต่อสังคม")))
      self.driver.find_element(By.LINK_TEXT, "ความรับผิดชอบต่อสังคม").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ความรับผิดชอบต่อสังคม"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "การกำกับดูแลกิจการ")))
      self.driver.find_element(By.LINK_TEXT, "การกำกับดูแลกิจการ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "การกำกับดูแลกิจการ"
      time.sleep(2)
      self.driver.find_element(By.ID, "navbarDropdown").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "โครงการในอนาคต")))
      self.driver.find_element(By.LINK_TEXT, "โครงการในอนาคต").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "โครงการในอนาคต"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "น้ำมันเครื่อง")))
      self.driver.find_element(By.LINK_TEXT, "น้ำมันเครื่อง").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "น้ำมันเครื่อง"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "สถานีบริการ")))
      self.driver.find_element(By.LINK_TEXT, "สถานีบริการ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "สถานีบริการ"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "SUSCO SQUARE")))
      self.driver.find_element(By.LINK_TEXT, "SUSCO SQUARE").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "SUSCO SQUARE"
      time.sleep(2)
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ส่งเสริมการขาย")))
      self.driver.find_element(By.LINK_TEXT, "ส่งเสริมการขาย").click()
      time.sleep(2)
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ส่งเสริมการขาย"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "หน้าหลักนักลงทุนสัมพันธ์")))
      self.driver.find_element(By.LINK_TEXT, "หน้าหลักนักลงทุนสัมพันธ์").click()
      time.sleep(2)
      #WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      #assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "INVESTOR RELATIONS\\\\nนักลงทุนสัมพันธ์"
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลทางการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "งบการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "งบการเงิน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "งบการเงิน"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลทางการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลสำคัญทางการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำคัญทางการเงิน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข้อมูลสำคัญทางการเงิน"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลทางการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "คำอธิบายและการวิเคราะห์")))
      self.driver.find_element(By.LINK_TEXT, "คำอธิบายและการวิเคราะห์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "คำอธิบายและการวิเคราะห์"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลทางการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "รายงานประจำปี")))
      self.driver.find_element(By.LINK_TEXT, "รายงานประจำปี").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "รายงานประจำปี"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลทางการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ฟอร์ม 56-1")))
      self.driver.find_element(By.LINK_TEXT, "ฟอร์ม 56-1").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ฟอร์ม 56-1"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลทางการเงิน")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน").click()
      self.vars["window_handles"] = self.driver.window_handles
      self.driver.find_element(By.LINK_TEXT, "หนังสือชี้ชวน").click()
      self.vars["win8174"] = self.wait_for_window(2000)
      self.vars["root"] = self.driver.current_window_handle
      self.driver.switch_to.window(self.vars["win8174"])
      self.driver.close()
      self.driver.switch_to.window(self.vars["root"])
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์").click()
      time.sleep(2)
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ราคาหลักทรัพย์")))
      self.driver.find_element(By.LINK_TEXT, "ราคาหลักทรัพย์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ราคาหลักทรัพย์"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ราคาหลักทรัพย์ย้อนหลัง")))
      self.driver.find_element(By.LINK_TEXT, "ราคาหลักทรัพย์ย้อนหลัง").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".symbol")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".symbol").text == "SUSCO"
      time.sleep(5)
      self.driver.execute_script("window.history.go(-1)")
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "เครื่องคำนวณการลงทุน")))
      self.driver.find_element(By.LINK_TEXT, "เครื่องคำนวณการลงทุน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "เครื่องคำนวณการลงทุน"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "หน้าหลักนักลงทุนสัมพันธ์")))
      self.driver.find_element(By.LINK_TEXT, "หน้าหลักนักลงทุนสัมพันธ์").click()
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือใบสำคัญแสดงสิทธิ")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือใบสำคัญแสดงสิทธิ").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข้อมูลสำหรับผู้ถือใบสำคัญแสดงสิทธิ"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "โครงสร้างผู้ถือหุ้น")))
      self.driver.find_element(By.LINK_TEXT, "โครงสร้างผู้ถือหุ้น").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "โครงสร้างผู้ถือหุ้น"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "การประชุมผู้ถือหุ้น")))
      self.driver.find_element(By.LINK_TEXT, "การประชุมผู้ถือหุ้น").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "การประชุมผู้ถือหุ้น"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "นโยบายจ่ายเงินปันผล")))
      self.driver.find_element(By.LINK_TEXT, "นโยบายจ่ายเงินปันผล").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "นโยบายจ่ายเงินปันผล"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลสำหรับผู้ถือหุ้น").click()
      #WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "สรุปข้อสนเทศ")))
      self.driver.find_element(By.LINK_TEXT, "สรุปข้อสนเทศ").click()
      time.sleep(4)
      #WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "www.susco.co.th")))
      #assert self.driver.find_element(By.LINK_TEXT, "www.susco.co.th").text == "www.susco.co.th"
      self.driver.execute_script("window.history.go(-1)")
      time.sleep(2)
      #self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ปฎิทินกิจกรรม")))
      self.driver.find_element(By.LINK_TEXT, "ปฎิทินกิจกรรม").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ปฏิทินกิจกรรม"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลนำเสนอแบบมัลติมีเดีย")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลนำเสนอแบบมัลติมีเดีย").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข้อมูลนำเสนอแบบมัลติมีเดีย"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข้อมูลบทวิเคราะห์")))
      self.driver.find_element(By.LINK_TEXT, "ข้อมูลบทวิเคราะห์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข้อมูลบทวิเคราะห์"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวสารบริษัท")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวแจ้งตลาดหลักทรัพย์")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวแจ้งตลาดหลักทรัพย์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข่าวแจ้งตลาดหลักทรัพย์"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวสารบริษัท")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวสารล่าสุด")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวสารล่าสุด").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข่าวสารล่าสุด"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวสารบริษัท")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวจากสื่อสิ่งพิมพ์")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวจากสื่อสิ่งพิมพ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข่าวจากสื่อสิ่งพิมพ์"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวสารบริษัท")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวสารบริษัท").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวประชาสัมพันธ์")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวประชาสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ข่าวประชาสัมพันธ์"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "สอบถามข้อมูล")))
      self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ข่าวสารทางอีเมล")))
      self.driver.find_element(By.LINK_TEXT, "ข่าวสารทางอีเมล").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "รับข่าวสารทางอีเมล"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "สอบถามข้อมูล")))
      self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ฝากคำถาม")))
      self.driver.find_element(By.LINK_TEXT, "ฝากคำถาม").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ฝากคำถาม"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "สอบถามข้อมูล")))
      self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "คำถามที่ถูกถามบ่อย")))
      self.driver.find_element(By.LINK_TEXT, "คำถามที่ถูกถามบ่อย").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "คำถามที่ถูกถามบ่อย"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "สอบถามข้อมูล")))
      self.driver.find_element(By.LINK_TEXT, "สอบถามข้อมูล").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ช่องทางการรับเรื่องร้องเรียน")))
      self.driver.find_element(By.LINK_TEXT, "ช่องทางการรับเรื่องร้องเรียน").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ช่องทางการรับเรื่องร้องเรียน"
      time.sleep(2)
      self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ติดต่อนักลงทุนสัมพันธ์")))
      self.driver.find_element(By.LINK_TEXT, "ติดต่อนักลงทุนสัมพันธ์").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".big-headSubText")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".big-headSubText").text == "ติดต่อนักลงทุนสัมพันธ์"
      WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "หน้าหลัก")))
      time.sleep(2)
    except Exception as e:
        # If an assertion error occurs, capture a screenshot and attach it to the Allure report
        allure.attach(self.driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
