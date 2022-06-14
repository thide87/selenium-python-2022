from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config

class TestDownload:
    
    def setup_method(self):
         # Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait utilizando la informacion de config.json
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_small())

        # Abrir la pagina web
        self.driver.get(config.get_url())
        
    def test_search_display(self):
        """Ejercicio 14"""
        
        etiqueta_desktop=(By.LINK_TEXT,'Desktops')
        etiqueta_desk : WebElement =self.wait.until(EC.element_to_be_clickable(etiqueta_desktop))
        assert etiqueta_desk.is_displayed(), 'No se encontro desktop'
        etiqueta_desk.click()

        select_mac=(By.LINK_TEXT,'Mac (1)')
        sel_mac : WebElement =self.wait.until(EC.element_to_be_clickable(select_mac))
        assert sel_mac.is_displayed(), 'No se encontro mac en la lista'
        sel_mac.click()
        
        element_encontrado=(By.LINK_TEXT,'iMac')
        element:WebElement=self.wait.until(EC.element_to_be_clickable(element_encontrado))
        assert element.is_displayed(),'No existe elemento uno'
        element.click()
        
        add_car=(By.ID,'button-cart')
        adding_car:WebElement=self.wait.until(EC.element_to_be_clickable(add_car))
        assert adding_car.is_displayed(),'No existe boton agregar'
        adding_car.click()
        
        mgs_succes=(By.CLASS_NAME,'alert-success')
        success='Success: You have added'
        assert self.wait.until(EC.text_to_be_present_in_element(mgs_succes,success))
        
        item_add=(By.XPATH,'//span[text()=" 1 item(s) - $122.00"]')
        assert self.wait.until(EC.text_to_be_present_in_element(item_add,"1 item(s) - $122.00")), "No se encuentra el texto esperado"
       
    def teardown_method(self):
        if self.driver:
            self.driver.quit()    