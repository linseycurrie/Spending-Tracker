
class User:

    def __init__(self, name, spending_limit, id=None):
        self.name = name
        self.spending_limit = spending_limit
        self.id = id

    def alert_near_limit(self, total):
        float_total = float(total)
        if (self.spending_limit == float_total):
            return "on"
        if ((self.spending_limit >= (float_total * 0.9)) and (self.spending_limit < float_total)):
            return "warning"
        elif (float_total > self.spending_limit) :
            return "over"
        else:
            return "ok"

