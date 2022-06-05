import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = "https://demoqa.com/select-menu"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Web Page
driver.get(url)

# Test Logic
time.sleep(2)
colors = driver.find_element(By.ID, "oldSelectMenu")
assert colors.is_displayed(), "Colors is not visible"
colors_dropdown = Select(colors)
colors_dropdown.select_by_visible_text("Green")
##saber si es seleccionada 
select_opt : WebElement = colors_dropdown.first_selected_option
assert select_opt.text == 'Green', 'Green is not selected'

#close
driver.quit()