from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        """Ejercicio 13"""
         
       
        input_search=(By.NAME,'search')
        search: WebElement =self.wait.until(EC.element_to_be_clickable(input_search))
        search.clear()
        search.send_keys('Display')
        
        busqueda=(By.XPATH,'//*[@id="search"]//button')
        busque: WebElement=self.wait.until(EC.element_to_be_clickable(busqueda))
        busque.click()
        
        display=(By.XPATH,'//p[text()="There is no product that matches the search criteria."]')
        assert self.wait.until(EC.text_to_be_present_in_element(display,"There is no product that matches the search criteria."))
       
        
        check_display=(By.ID,'description')
        check_dis:WebElement=self.wait.until(EC.visibility_of_element_located(check_display))
        assert check_dis.is_displayed(),'No existe checkbox'
        check_dis.click()
        assert check_dis.is_selected()
        
        button_display=(By.ID,'button-search')
        button_dis:WebElement=self.wait.until(EC.element_to_be_clickable(button_display))
        assert button_dis.is_displayed(),'No existe boton de busqueda'
        button_dis.click()
        
        for product in ['Apple Cinema 30"','iPod Nano','iPod Touch','MacBook Pro']:
            loc=(By.LINK_TEXT,product)
            self.wait.until(EC.element_to_be_clickable(loc))        
                    
    def teardown_method(self):
        if self.driver:
            self.driver.quit() 