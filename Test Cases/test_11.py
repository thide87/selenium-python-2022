from webbrowser import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.factory.factory_driver import get_driver


driver: WebDriver = None

def setup():
    global driver
    driver = get_driver()
    
def test_search_iphone():
    driver.get("https://laboratorio.qaminds.com/")
    telefonos= driver.find_element(By.LINK_TEXT,'Phones & PDAs')
    assert telefonos.is_displayed, 'No se encontro la opcion de telefonos'
    telefonos.click()
    
    iphone=driver.find_element(By.LINK_TEXT,'iPhone')
    assert iphone.is_displayed, 'No se encontro el telefono iphone'
    
def test_search_tablet():
    driver.get("https://laboratorio.qaminds.com/")    
    tablets=driver.find_element(By.LINK_TEXT,'Tablets')
    assert tablets.is_displayed(),'No se encontro la etiqueta tablet'
    tablets.click()
    
    samsung=driver.find_element(By.LINK_TEXT,'Samsung Galaxy Tab 10.1')
    assert samsung.is_displayed(), 'No se encontro la tablet samsung'
    
def test_windows():
    driver.get("https://laboratorio.qaminds.com/")
    header = driver.find_element(By.PARTIAL_LINK_TEXT, 'Laptops')
    header.click()
    sub_header = driver.find_element(By.PARTIAL_LINK_TEXT, 'Windows')
    sub_header.click()
    windows = driver.find_element(By.XPATH, "//*[@id='content']/p")
    assert windows.text == 'There are no products to list in this category.', 'Products were found'

def teardown():
    if driver:
        driver.quit()
