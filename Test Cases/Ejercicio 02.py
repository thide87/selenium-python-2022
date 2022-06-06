#EJERCICIO 2:
#Ir a la página https://laboratorio.qaminds.com/
#Escribir un script que:
#Seleccione la opción Tablets
#Deberá aparecer un item con titulo: Samsung Galaxy Tab 10.1
#Seleccionar dicho item
#Verifique que:
#El costo del item es de $241.99
#Puede agregarlo a una Whist List
#Puede agregarlo al Carrito


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://laboratorio.qaminds.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Abrir pagina
driver.get(url)
time.sleep(3)


#buscador 
word = "iphone"
time.sleep(5)
opc_tablet : WebElement = driver.find_element(By.LINK_TEXT,'Tablets')
assert opc_tablet.is_displayed(), "no visible"
opc_tablet.click()

la_tablet : WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, 'Samsung Galaxy Tab 10.1')
assert la_tablet.is_displayed(), "no visible tablet"
la_tablet.click()

costo : WebElement = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2') #mejorar xpath..
assert costo.is_displayed(), "no existe el valor"
assert costo.text == "$241.99", "el precio no es de 241.99 "


wish_list : WebElement = driver.find_element(By.XPATH, '//button[@data-original-title="Add to Wish List"]')
assert wish_list.is_displayed(), "no existe boton wish"
wish_list.click()

add_car : WebElement = driver.find_element(By.XPATH, '//*[@id="button-cart"]')
assert add_car.is_displayed(), "no existe boton car"
add_car.click()


# Cerrar navegador
#driver.quit()