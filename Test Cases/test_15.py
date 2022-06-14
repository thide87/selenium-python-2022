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
        """Ejercicio 15"""
        
        locator_label=(By.XPATH,'//strong[text()="$"]')
        assert self.wait.until(EC.text_to_be_present_in_element(locator_label,"$")), "$ no se muestra en la currency"

        input_search=(By.NAME,'search')
        search: WebElement =self.wait.until(EC.element_to_be_clickable(input_search))
        search.clear()
        search.send_keys('Samsung')
        
        busqueda=(By.XPATH,'//*[@id="search"]//button')
        button_busqueda: WebElement=self.wait.until(EC.element_to_be_clickable(busqueda))
        button_busqueda.click()
        
        item_samsung=(By.LINK_TEXT,'Samsung SyncMaster 941BW')
        item_sam:WebElement=self.wait.until(EC.element_to_be_clickable(item_samsung))
        item_sam.click()
        
        currency_select=(By.ID,'form-currency')
        currency_sel:WebElement=self.wait.until(EC.element_to_be_clickable(currency_select))
        currency_sel.click()
        
        price_dollar=(By.XPATH,'//*[@class="list-unstyled"]//li//h2')
        text_dollar="$242.00"
        cantidad_dollar=float(text_dollar[1:])
        print(cantidad_dollar)
        dollar:WebElement=self.wait.until(EC.visibility_of_any_elements_located(price_dollar))
        
        currency_euro=(By.NAME,'EUR')
        currency_eur:WebElement=self.wait.until(EC.visibility_of_element_located(currency_euro))
        currency_eur.click()
       
        price_eur=(By.XPATH,'//*[@class="list-unstyled"]//li//h2')
        text_eur="189.87€"
        cantidad_eur=float(text_eur[:-1])
        price_eur:WebElement=self.wait.until(EC.visibility_of_any_elements_located(price_eur))
        assert cantidad_eur<cantidad_dollar

    def teardown_method(self):
        if self.driver:
            self.driver.quit()