import unittest
from models.user import User

class TestTask(unittest.TestCase):

    def setUp(self):
        self.user = User("John", 20.00, 30,00)

