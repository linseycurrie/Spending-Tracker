import pdb

from models.merchant import Merchant
from models.transaction import Transaction
from models.user import User
from models.category import Category

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import repositories.category_repository as category_repository

user1 = User("John", 20.00, 30.00)


user_repository.save(user1)


merchant1 = Merchant("Tesco", "Glasgow")
merchant2 = Merchant("Oasis", "Edinburgh")
merchant3 = Merchant("Asda", "Glasgow")

merchant_repository.save(merchant1)
merchant_repository.save(merchant2)
merchant_repository.save(merchant3)

category1 = Category("Grocieres")
category2 = Category("Clothing")
category3 = Category("Fuel")

category_repository.save(category1)
category_repository.save(category2)
category_repository.save(category3)

transaction1 = Transaction(25.00, category2, "2020-09-22", merchant1, user1)
transaction2 = Transaction(5.00, category1, "2020-01-12",  merchant2, user1)
transaction3 = Transaction(10.00, category3, "2020-02-15", merchant3, user1)

transaction_repository.save(transaction1)
transaction_repository.save(transaction2)
transaction_repository.save(transaction3)



