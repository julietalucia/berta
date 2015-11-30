from berta.parametrizedtestcase import ParametrizedTestCase
import unittest
from berta.basepage import BasePage
from sample.code.mainpage import MainPage
import time

class TestSearch(ParametrizedTestCase):

	def test_search_fail(self):
		page = MainPage()
		page = page.getpageobject()
		page = page.search(self.param)
		time.sleep(3)
		self.assertIn('Nothing Found', page.source())

	def test_search_successful(self):
		page = MainPage().getpageobject()
		page = page.search(self.param)
		time.sleep(3)
		self.assertIn('Search Results for', page.source())

	def test_search_and_click_successful(self):
		self.test_search_successful()
		page = MainPage().getpageobject()
		page.select_first_result()
		

