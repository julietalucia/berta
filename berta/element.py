import importlib
import yaml
from config import pageobject_parser,parameters
from contextlib import contextmanager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BaseElement(object):
    driver = None
    def __init__(self, locator = None):
        self.locator = locator
        self.timeout = 60

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        """Taken from Harry Percival's solution to the """
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        try:
            WebDriverWait(self.driver, timeout).until(staleness_of(old_page))
        except TimeoutException:
            pass

    def mouseover(self):
        element = self.driver.find_element(By.XPATH, self.locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def press_key(self, press_key):
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(By.XPATH, self.locator)) 
        self.driver.find_element(By.XPATH, self.locator).send_keys(Keys.__dict__[press_key])

class InputElement(BaseElement): 
    def set(self, value): 
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(By.XPATH, self.locator)) 
        #clears the input before sending keys
        try:
            self.driver.find_element(By.XPATH, self.locator).clear()
        finally:
            self.driver.find_element(By.XPATH, self.locator).send_keys(value)

    def get(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(By.XPATH, self.locator))
        element = self.driver.find_element(By.XPATH, self.locator)
        return element.get_attribute("value")

class SelectElement(BaseElement): 
    def select(self, value): 
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(By.XPATH, self.locator)) 
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(By.XPATH, self.locator + '/option'))
        if (isinstance(value,str)==False):
            Select(self.driver.find_element(By.XPATH, self.locator)).select_by_index(value)
        else:
            Select(self.driver.find_element(By.XPATH, self.locator)).select_by_visible_text(value)



class ButtonElement(BaseElement):
    def click(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(By.XPATH, self.locator)) 
        self.driver.find_element(By.XPATH, self.locator).click()
    
            

class CheckBoxElement(ButtonElement):
    def check(self):
        self.click()

class RadioButtonElement(ButtonElement):
    def select(self):
        self.click()

class LinkElement(ButtonElement):
    pass

class BaseForm(object):
    driver = None
    def __init__(self, config): 
        """Read the received dictionary and create dinamically the elments of the form needed"""
        for k, v in config.items():
            if 'input' in k:
                self.__dict__[k] = InputElement(v)
            elif 'checkbox' in k:
                self.__dict__[k] = CheckBoxElement(v)
            elif 'button' in k:
                self.__dict__[k] = ButtonElement(v)
            elif 'radiobutton' in k:
                self.__dict__[k] = RadioButtonElement(v)
            elif  'select' in k:
                 self.__dict__[k] = SelectElement(v)
            else:
                pass

    def load (self,data = None):
        """Load the received parameters to the form previously created"""
        if data == None:
            return
        for k,v in data:
            if 'input' in k:
                self.__dict__[k].set(v)
            elif 'radiobutton' in k:
                self.__dict__[k].click()
            elif 'checkbox' in k:
                self.__dict__[k].check()
            elif 'button' in k:
                self.__dict__[k].click()
            elif 'select' in k: 
                self.__dict__[k].select(v)
            else:
                pass
    def submit(self):
        """Click on the submit_button. The submit_button must have that specific name"""
        with self.submit_button.wait_for_page_load():
            self.submit_button.click()
        
    
class Menu(object):     
    driver = None
    def __init__(self):
        try:
            module = importlib.import_module(parameters['SERIALIZATION_LANGUAGE'])
            with open(parameters['MENU_PATH']) as file:
                self.configuracion_de_menu = module.load(file)
        except Exception as Ex:
            print(str(Ex))
            
        
    def click_option(self, opcion):
        boton1 = ButtonElement (self.configuracion_de_menu[opcion])
        boton1.click()    
    

        
        
    



    
