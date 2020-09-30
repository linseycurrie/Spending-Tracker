
class User:

    def __init__(self, name, spending_limit, id=None):
        self.name = name
        self.spending_limit = spending_limit
        self.id = id

    def alert_near_limit(self, total):
        float_total = float(total)
        print(float_total * 0.9)
        if (self.spending_limit == float_total):
            return "on"
        elif (float_total > self.spending_limit) :
            return "over"
        elif ((float_total * 0.9) < self.spending_limit > float_total):
            return "warning"
        else:
            return "ok"

