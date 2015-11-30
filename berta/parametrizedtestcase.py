import unittest
from selenium import webdriver
from berta.basepage import BasePage
from sample.code.mainpage import MainPage

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
	This solution's been taken from Eli Benderesky's site (http://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases)
	It has been slightly modified to suit the needs of the project
    """
		
    def __init__(self, methodName='runTest', param = None):
        super(ParametrizedTestCase, self).__init__(methodName)
        for k,v in param.items():
        	self.__dict__[k]= v

    @staticmethod
    def parametrize(testcase_klass, testname, **kwargs):
        """ Receive a class and that class' method 
		Optionally, it can receive N parameters that are passed to the test
        """
        testloader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTest(testcase_klass(testname, kwargs))
        return suite
