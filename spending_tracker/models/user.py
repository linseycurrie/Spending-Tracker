
class User:

    def __init__(self, name, spending_limit=None, savings_goal=None, id=None):
        self.name = name
        self.spending_limit = spending_limit
        self.savings_goal = savings_goal
        self.id = id

    def alert_near_limit(self, total):
        if self.spending_limit >= (total * 0.9):
            return True