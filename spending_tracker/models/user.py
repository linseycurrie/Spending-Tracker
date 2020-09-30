
class User:

    def __init__(self, name, spending_limit, id=None):
        self.name = name
        self.spending_limit = spending_limit
        self.id = id

    def alert_near_limit(self, total):
        float_total = float(total)
        float_spending_limit = float(self.spending_limit)
        print(float_spending_limit * 0.9)
        if (self.spending_limit == float_total):
            return "on"
        elif (self.spending_limit < float_total) :
            return "over"
        elif ((0.9 * float_spending_limit) < float_total):
            return "warning"
        else:
            return "ok"

