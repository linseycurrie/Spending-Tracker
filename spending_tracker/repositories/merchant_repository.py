from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, location, activated) VALUES ( %s, %s, %s ) RETURNING *"
    values = [merchant.name, merchant.location, merchant.activated]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select_all():
    merchants =[]

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant( row['name'], row['location'], row['activated'], row['id'] )
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant( result['name'], result['location'], result['activated'], result['id'] )
    return merchant

def update(merchant):
    sql = "UPDATE merchants SET (name, location, activated) = ( %s, %s, %s ) WHERE id = %s"
    values = [merchant.name, merchant.location, merchant.activated, merchant.id]
    print(values)
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)