#EJERCICIO 1:
#Ir a la página https://laboratorio.qaminds.com/
#Escribir un script que:
#Permita buscar un iphone desde la barra de búsqueda
#Verificar que devuelve un resultado con una imagen que pertenece a un iphone

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Inicializar driver
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://laboratorio.qaminds.com/'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
driver.maximize_window()

# Abrir pagina
driver.get(url)
time.sleep(3)

word = "iphone"
#buscador 
driver.implicitly_wait(5)
search_barra : WebElement = driver.find_element(By.XPATH,'//*[@id="search"]/input')
assert search_barra.is_displayed(), "barra no visible"
search_barra.clear()
search_barra.send_keys(word)

button_search : WebElement = driver.find_element(By.XPATH, '//*[@id="search"]//button')
assert button_search.is_displayed, "no existe el boton"
button_search.click()
by_img : WebElement = driver.find_element(By.XPATH,'//img[@alt="samsung"]')
assert by_img.is_displayed(), "no esta la imagen"


# Cerrar navegador
driver.quit()