
class User:

    def __init__(self, name, spending_limit, savings_goal, id=None):
        self.name = name
        self.spending_limit = spending_limit
        self.savings_goal = savings_goal
        self.id = id

    def alert_near_limit(self, total):
        if self.spending_limit != None:
            print(self.spending_limit)
            float_total = float(total)
            while self.spending_limit > (float_total * 0.9):
                return False
        return True