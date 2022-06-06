#Ejercicio 10:
#Construir un test que :
#Abra la pagina: https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html
#Presione el la opción Autocloseable success message
#Verificar que se muestra mensaje
#Verificar que mensaje mostrado desaparece después de 5 segundos.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import  get_driver

get_driver("chrome")

url = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'

#service = Service(gecko_driver_path)

driver = webdriver.Firefox(service=service)

wait = WebDriverWait(driver, 15)

# Open Web Page
driver.get(url)


locator = (By.ID,"autoclosable-btn-success" )
btn : WebElement = wait.until(EC.element_to_be_clickable(locator))
btn.click()

tx_ONE = (By.CLASS_NAME,"alert-autocloseable-success") 

wait.until(EC.visibility_of_element_located(tx_ONE))

assert  wait.until(EC.invisibility_of_element_located(tx_ONE)), "element visible"


#CLose browser
driver.quit()