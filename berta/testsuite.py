import unittest 
from selenium import webdriver
from berta.basepage import BasePage
from config import parameters

class TestSuite(unittest.TestSuite):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get(parameters['PROJECT_URL'])
		self.driver.maximize_window()
		BasePage.driver = self.driver

	def tearDown(self):
		self.driver.close()

	def run(self, result):
		self.setUp()
		super().run(result)
		self.tearDown()	
