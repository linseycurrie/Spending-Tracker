import unittest

from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("John", 100.00)
        

    def test_alert_near_limit_Under_warning(self):
        total = 50
        self.assertEqual("ok", self.user.alert_near_limit(total))

    def test_alert_near_limit_warning(self):
        total = 105
        self.assertEqual("warning", self.user.alert_near_limit(total))

    def test_alert_near_limit_over_limit(self):
        total = 150
        self.assertEqual("over", self.user.alert_near_limit(total))

    def test_alert_near_limit_over(self):
        total = 100
        self.assertEqual("on", self.user.alert_near_limit(total))

    

