from berta.basepage import BasePage
from berta.element import *

class Wplogin(BasePage):
    def login(self, login_data):
        form = BaseForm(self.config['LoginForm'])
        form.load(login_data)
        form.submit()
        return self.getpageobject()

        
