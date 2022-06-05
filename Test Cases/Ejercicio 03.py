#Ejercicio 3:
#Ir a la página https://laboratorio.qaminds.com/
#Escribir un script que:
#Desde la página principal pueda ir a la sección Login
#Dado un login invalido se muestre un cartel de error con el mensaje:
#“Warning: No match for E-Mail Address and/or Password.”


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
time.sleep(5)

my_account: WebElement = driver.find_element(By.LINK_TEXT, "My Account")#or con xpath other exaple for looging the other acount is: //footer//a[normalize-space(.)='My Account']
assert my_account.is_displayed(), "my account is not visible"
my_account.click()

opc_login: WebElement = driver.find_element(By.LINK_TEXT, "Login")
assert opc_login.is_displayed(), "login is not visible"
opc_login.click()

correo : WebElement = driver.find_element(By.NAME, "email")
assert correo.is_displayed(), "correo is not visible"
correo.clear()
correo.send_keys("casa")

password : WebElement = driver.find_element(By.ID, "input-password")
assert password.is_displayed(), "password is not visible"
password.clear()
password.send_keys("casas")



login_btn = WebElement = driver.find_element(By.XPATH, '//input[@value="Login"]')
assert login_btn.is_displayed(), "login is not visible"
login_btn.click()

clase_error : WebElement = driver.find_element(By.XPATH,"//*[contains(@class,'fa-exclamation-circle')]")#too find by.CSS ej: .fa-exclamation-circle
assert clase_error.is_displayed(),"no hay error"
assert clase_error.text == " Warning: No match for E-Mail Address and/or Password.", "no coincide el texto de error"


# Close browser
#driver.quit()