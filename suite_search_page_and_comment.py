#!/usr/bin/python3
import random
import unittest 
from tests.testsearch import TestSearch
from tests.testcomment import TestComment
from berta.parametrizedtestcase import ParametrizedTestCase
from berta.testsuite import TestSuite

the_simpsons_search_data = 'Maggie'
animal_search_data = 'Animal'
comment_data = [('comment_input',str(random.random())),('name_input', 'Troll'),('email_input', 'troll@troll.com')]

suite = TestSuite()
random.seed()
"""You can choose to pass the suite as many parameters as you want, as long as you use them in the TestCase.
For example: you can do ParametrizedTestCase.parametrize(YourTestCase, testname = thetestmethodyouarecalling, param1 = example, param2 = example)
Then in YourTestCase you can use param1 and param2 as variables."""
suite.addTest(ParametrizedTestCase.parametrize(TestSearch, 
		testname = "test_search_fail", param = the_simpsons_search_data))

suite.addTest(ParametrizedTestCase.parametrize(TestSearch, 
		testname = "test_search_and_click_successful", param = animal_search_data))

suite.addTest(ParametrizedTestCase.parametrize(TestComment,
		 testname = "test_comment_successful",param = comment_data))

unittest.TextTestRunner(verbosity=2).run(suite)



