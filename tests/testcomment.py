from berta.parametrizedtestcase import ParametrizedTestCase
import unittest
from berta.basepage import BasePage
from sample.code.mainpage import MainPage
import time

class TestComment(ParametrizedTestCase):

    def test_comment_successful(self):
        page = MainPage().getpageobject()
        page.leave_comment(self.param)
        #assert missing



