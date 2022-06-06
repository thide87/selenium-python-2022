#Ejercicio 3:
#Ir a la página https://laboratorio.qaminds.com/
#Escribir un script que:
#Desde la página principal pueda ir a la sección Login
#Dado un login invalido se muestre un cartel de error con el mensaje:
#“Warning: No match for E-Mail Address and/or Password.”

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#Inicializa driver
chrome_driver_path='./drivers/chromedriver'
gecko_driver_path='./drivers/geckodriver'
url='https://laboratorio.qaminds.com/'
service =Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
#Abrir Pag
driver.get(url)
time.sleep(3)
#Login Invalido
mi_cuenta : WebElement =driver.find_element(By.LINK_TEXT,'My Account')
assert mi_cuenta.is_displayed(), 'No se encontro'
mi_cuenta.click()

login : WebElement =driver.find_element(By.LINK_TEXT,'Login')
assert login.is_displayed(), 'No se login para iniciar sesion'
login.click()
time.sleep(4)

email:WebElement= driver.find_element(By.ID,'input-email')
assert email.is_displayed(), 'No se encontro campo de email'
email.send_keys('correo@mail.com')

password:WebElement= driver.find_element(By.ID,'input-password')
assert password.is_displayed(), 'No se encontro campo de password'
password.send_keys('123456789')

button_login :WebElement=driver.find_element(By.XPATH,'//*[@value="Login"]') #cambiar xpath
assert button_login.is_displayed(), 'No encontro boton'
button_login.click()
#Warring 
warning:WebElement=driver.find_element(By.XPATH,'//*[contains(@class,"fa-exclamation-circle")]')#cambiar xpath
assert warning.is_displayed(),'No mostro warning'

driver.quit()