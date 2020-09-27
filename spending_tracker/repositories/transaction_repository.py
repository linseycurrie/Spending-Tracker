from db.run_sql import run_sql
from models.user import User
from models.merchant import Merchant
from models.transaction import Transaction
from models.category import Category
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, category_id, date, merchant_id) VALUES ( %s, %s, %s, %s ) RETURNING *"
    values = [transaction.amount, transaction.category.id, transaction.date, transaction.merchant.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():
    transactions =[]

    sql= "SELECT * FROM transactions"
    results = run_sql(sql)
    
    for row in results:
        merchant = merchant_repository.select( row['merchant_id'] )
        category = category_repository.select( row['category_id'])
        transaction = Transaction( row['amount'], category, row['date'], merchant, row['id'] )
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction( result['amount'], category, result['date'], merchant, result['id'])
    return transaction

def update(transaction):
    sql = "UPDATE transactions SET (amount, category_id, date, merchant_id) = ( %s, %s, %s, %s ) WHERE id = %s"
    values = [transaction.amount, transaction.category.id, transaction.date, transaction.merchant.id, transaction.id]
    print(values)
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def total_amount(transactions):
    total = 0
    for transaction in transactions:
        total += transaction.amount
    return total

# def sort_by_month(transactions, month):
#     transactions = []
#     for transaction in transactions:
#         date = transaction.date.split('-')
#         if date[2] == month:
#             transactions.append(transaction)
#     return transactions