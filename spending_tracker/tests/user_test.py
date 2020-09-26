import unittest
from models.user import User

class TestTask(unittest.TestCase):

    def setUp(self):
        self.user = User("John", 20.00, 30,00)

    def test_user_has_name(self):
        self.assertEqual("John", self.user.name)

    def test_user_can_set_spending_limit(self):
        self.assertEqual(20.00, self.user.spending_limit)

    def test_user_can_set_savings_goal(self):
        self.assertEqual(30.00, self.user.savings_goal)