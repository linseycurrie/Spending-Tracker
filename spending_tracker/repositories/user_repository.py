from db.run_sql import run_sql
from models.merchant import Merchant
from models.transaction import Transaction

def save(user):
    sql = "INSERT INTO users(name) VALUES ( %s ) RETURNING id"
    values = [user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user