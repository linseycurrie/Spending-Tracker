
class Transaction:

    def __init__(self, amount, category, merchant, id=None):
        self.amount = amount
        self.category = category
        self.merchant = merchant
        self.id = id