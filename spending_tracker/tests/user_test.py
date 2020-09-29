import unittest

from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("John", 50.00)
        self.user1 = User("Betty", 95.00)
        self.user2 = User("Sue", 105.00)
        

    def test_alert_near_limit_Under_warning(self):
        total = 100
        self.assertEqual("ok", self.user.alet_near_limit(total))

    def test_alert_near_limit_warning(self):
        total = 100
        self.assertEqual("warning", self.user1.alert_near_limit(total))

    def test_alert_near_limit_Under_over_limit(self):
        total = 100
        self.assertEqual("over", self.user2.alert_near_limit(total))

    

