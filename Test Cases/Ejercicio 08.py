#Ejercicio 8:
#Construir un test que :
#Abra la pagina: https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html
#Presione el botón Start Download y espere a que se realice la descarga.
#Verificar que aparece el mensaje: Complete
#Verificar que aparece el botón Close

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
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)

locator = (By.ID,"downloadButton" )
search_btn : WebElement = wait.until(EC.element_to_be_clickable(locator))
search_btn.click()

tx_complete = (By.CSS_SELECTOR, ".progress-label" ) #XPATH: //*[@class='progress-label']
assert  wait.until(EC.text_to_be_present_in_element(tx_complete, "Complete!")), "yet not completed"

#verificar el boton continue}
cls_btn = (By.XPATH, "//button[text()='Close']")
cls_btn : WebElement = wait.until(EC.element_to_be_clickable(cls_btn))
cls_btn.click()

#CLose browser
driver.quit()