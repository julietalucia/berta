from berta.parametrizedtestcase import ParametrizedTestCase
import unittest
from selenium import webdriver
from berta.basepage import BasePage
from sample.code.mainpage import MainPage

class TestSettings(ParametrizedTestCase):
	def test_setting(self):
		page = MainPage()
		page = page.getpageobject()
		page = page.delete_comment_by_email()
		page.driver.close()
		
	def tearDown(self):
		pass

if __name__ == "__main__":
    unittest.main()
