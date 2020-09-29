
class Transaction:

    def __init__(self, amount, category, date, merchant, id=None):
        self.amount = amount
        self.category = category
        self.date = date
        self.merchant = merchant
        self.id = id