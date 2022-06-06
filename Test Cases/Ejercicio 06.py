#Ejercicio 6:
#Ir a la página https://demoqa.com/select-menu
#Escribir un script que:
#seleccione de la primera lista Standard Multi Select las opción “Volvo” y “Audi”
#verifique que la opción ha sido seleccionada.

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
stile = driver.find_element(By.ID, "cars")
assert stile.is_displayed(), "stiles are not visible"
stile_dropdown = Select(stile)
stile_dropdown.select_by_visible_text("Volvo")
stile_dropdown.select_by_visible_text("Audi")

selected_options: list = [item.text for item in stile_dropdown.all_selected_options]
assert "Volvo" in selected_options, "Volvo is not selected"
assert "Audi" in selected_options, "Audi is not selected"


##saber 
#close
driver.quit()