from berta.basepage import BasePage
from berta.element import *
        
class MainPage(BasePage):
    def login(self, login_data):
        form = BaseForm(self.config['LoginForm'])
        form.load(login_data)
        form.submit()
        return self.getpageobject()

    def leave_comment(self, comment_data):
        form = BaseForm(self.config['ReplyForm'])
        form.load(comment_data)
        form.submit()
        return self.getpageobject()    

    def search(self, search_words):
        search_field = InputElement(self.config['search_input'])
        search_field.set(search_words)
        search_field.press_key('RETURN')
        return self.getpageobject()

    def select_first_result(self):
        result = LinkElement(self.config['first_result_link'])
        result.click()
        return self.getpageobject()

    def password_recover(self, mail):
        pass
        
