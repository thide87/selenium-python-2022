from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config

class TestDownload:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())
        
    def test_download_button_1(self):
        """Ejercicio 8"""
        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
        
        locator=(By.ID,'downloadButton')
        btn_descarga:WebElement=self.wait.until(EC.element_to_be_clickable(locator))
        assert btn_descarga.is_displayed, 'El boton no esta disponible'
        btn_descarga.click()

        locator_label=(By.XPATH,'//*[@class="progress-label"]')
        assert self.wait.until(EC.text_to_be_present_in_element(locator_label, "Complete!")), 'Complete no se muestra'

        locator_btn=(By.XPATH,'//*[@class="ui-dialog-buttonset"]/button')
        complete_btn:WebElement=self.wait.until(EC.element_to_be_clickable(locator_btn))
        assert complete_btn.is_enabled, 'El boton close no esta habilitado' 
          
    def test_download_button_2(self):
        """Ejercicio 9"""
        # Open web page
        self.driver.get('https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html')
        
        locator=(By.ID,'cricle-btn')
        btn_descarga:WebElement=self.wait.until(EC.element_to_be_clickable(locator))
        assert btn_descarga.is_displayed, 'El boton no esta disponible'
        btn_descarga.click()

        locator_label=(By.CSS_SELECTOR,'.percenttext')
        assert self.wait.until(EC.text_to_be_present_in_element(locator_label,"100%")), "100 no se muestra en pantalla"

        
    def test_auto_closable_msg(self):
        """Ejercicio 10"""
        # Open web page
        self.driver.get('https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html')
        locator=(By.ID,'autoclosable-btn-success')
        btn_success:WebElement=self.wait.until(EC.element_to_be_clickable(locator))
        assert btn_success.is_displayed, 'El boton no esta disponible'
        btn_success.click()

        locator_msg=(By.CSS_SELECTOR,'.alert-autocloseable-success')
        assert self.wait.until(EC.visibility_of_element_located(locator_msg))

        assert self.wait.until(EC.invisibility_of_element_located(locator_msg)),'Se sigue mostrando el mensaje'
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()