import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement

chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://qamindslab.com'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get("https://laboratorio.qaminds.com/")
time.sleep(5)

# Test Logic
laptop : WebElement = driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
assert laptop.is_displayed(), "no hay opcion lapton"
laptop.click()

opc_win : WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, "Windows")
assert opc_win.is_displayed(), "windows is not visible"
opc_win.click()

time.sleep(5)
content = driver.find_element(By.XPATH, "//*[@id='content']/p")
assert content.is_displayed(), "content is not visible"
assert content.text == "There are no products to list in this category.", "windows is not empty"

time.sleep(5)
continue_btn : WebElement = driver.find_element(By.LINK_TEXT, "Continue")
assert continue_btn.is_displayed(), "continue is not visible"
continue_btn.click()