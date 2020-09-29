
class User:

    def __init__(self, name, spending_limit, id=None):
        self.name = name
        self.spending_limit = spending_limit
        self.id = id

    def alert_near_limit(self, total):
        print(self.spending_limit)
        float_total = float(total)
        print(float_total)
        print(float_total * 0.9)
        if ((self.spending_limit >= (float_total * 0.9)) and (self.spending_limit <= total)):
            return "warning"
        elif (total > self.spending_limit) :
            return "over"
        else:
            return "ok"

