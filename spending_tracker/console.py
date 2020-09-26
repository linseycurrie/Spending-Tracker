import pdb

from models.merchant import Merchant
from models.transaction import Transaction
from models.user import User

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

user1 = User("John", 20.00, 30.00)
user2 = User("Sue", 20.00, 10.00)

tesco = Merchant("Tesco", "Glasgow")
oasis = Merchant("Oasis", "Edinburgh")
asda = Merchant("Asda", "Glasgow")
goOutdoors = Merchant("Go Outdoors", "Clydebank")

transaction1 = Transaction(25.00, "Clothing", tesco)
transaction2 = Transaction(5.00, "Groceres",  oasis)


user_repository.save(user1)
user_repository.save(user2)

merchant_repository.save(tesco)
merchant_repository.save(oasis)
merchant_repository.save(asda)
merchant_repository.save(goOutdoors)

transaction_repository.save(transaction1)
transaction_repository.save(transaction2)



