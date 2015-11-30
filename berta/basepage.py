import importlib
from config import pageobject_parser,parameters
from berta.element import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import NoSuchElementException
    
        
class BasePage(object):
    driver = None
    menu = Menu()
    def __init__(self):
        BaseElement.driver = self.driver
        BaseForm.driver = self.driver
        filename = self.__class__.__name__
        file_path = parameters['DATA_PATH']
        module = importlib.import_module(parameters['SERIALIZATION_LANGUAGE'])
        file_path = file_path + filename + '.' + parameters['SERIALIZATION_LANGUAGE']
        with open(file_path) as file:
            self.config = module.load(file)
        
    def getpageobject(self):
        """Call function pageobject_parser (made by user), in config.py """
        module, pageobjectname = pageobject_parser(self.driver.current_url, self.driver)
        module = importlib.import_module(module)
        currentpageobject = module.__dict__[pageobjectname]() 
        return currentpageobject

    def source(self):
        return self.driver.page_source
    
    def click_option_on_menu(self, option):
        """Click a menu's option"""
        self.menu.click_option(option)
        return self.getpageobject()
    
    def open_modal(self, option):
        """Receive as option the name of the button that opens the modal.
        Return the pageobject"""
        button = ButtonElement(self.config[option])
        button.click()
        self.driver.switch_to_default_content()    
        return self.getpageobject()
        
    def close_modal(self):
        close = ButtonElement(self.config['close_button'])
        try:
            close.click()
            self.driver.switch_to_default_content()
        except NoSuchElementException:
            self.driver.switch_to_default_content()
            close.click()
        finally:
            return self.getpageobject()    
