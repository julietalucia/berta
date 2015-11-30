from berta.parametrizedtestcase import ParametrizedTestCase
import unittest
from berta.basepage import BasePage
from sample.code.mainpage import MainPage

class TestLogin(ParametrizedTestCase):

	def test_login(self):
		page = MainPage()
		page = page.click_option_on_menu("login_link")
		page = page.login(self.param)
		self.assertIn('Wpadmin',str(type(page)))


