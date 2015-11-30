from berta.basepage import BasePage
from berta.element import BaseForm,LinkElement
from config import parameters
import importlib

class WordPressPage(BasePage):
    def __init__(self):
        super().__init__()
        filename = 'WordPressPage'
        file_path = parameters['DATA_PATH']
        module = importlib.import_module(parameters['SERIALIZATION_LANGUAGE'])
        file_path = file_path + filename + '.' + parameters['SERIALIZATION_LANGUAGE']
        with open(file_path) as file:
                self.config.update(module.load(file)) 
        print (self.config)

    def leave_comment(self, comment_data):
        comment_link = LinkElement(self.config['comment_link'])
        comment_link.click()
        formulario = BaseForm(self.config['ReplyForm'])
        formulario.load(comment_data)
        formulario.submit()
        return self.getpageobject()
