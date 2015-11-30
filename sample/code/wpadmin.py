from berta.basepage import BasePage
from berta.element import BaseForm
from berta.element import ButtonElement
        
class Wpadmin(BasePage):
    def change_general_settings(self, data):
        pass

    def change_writing_settings(self,data):
        settings_link = ButtonElement(self.config['settings_link'])
        settings_link.click()
        writing_option = ButtonElement(self.config['writing_link'])
        writing_option.click()    
        form = BaseForm(self.config['WrittingSettingsForm'])
        form.load(data)
        form.submit()
        return self.getpageobject()

    def delete_comment_by_email(self):
        ButtonElement(self.config['comments_link']).click()
        ButtonElement(self.config['comment_button']).mouseover()
        ButtonElement(self.config['delete_link']).click()
        return self.getpageobject()
