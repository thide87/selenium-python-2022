#Ejercicio 9:
#Construir un test que :
#Abra la pagina: https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html
#Presione el botón Download y espere a que se realice la descarga.
#Verificar que la descarga se realizó al 100%

from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 15)

# Open Web Page
driver.get(url)

locator = (By.ID,"cricle-btn" )
search_btn : WebElement = wait.until(EC.element_to_be_clickable(locator))
search_btn.click()

tx_ONE = (By.XPATH, "//*[@class='percenttext']" ) 
assert  wait.until(EC.text_to_be_present_in_element(tx_ONE, "100%")), "yet not completed"

#CLose browser
driver.quit()