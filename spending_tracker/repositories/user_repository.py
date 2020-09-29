from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users(name, spending_limit, savings_goal) VALUES ( %s, %s, %s ) RETURNING id"
    values = [user.name, user.spending_limit, user.savings_goal]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user

def select_all():
    users =[]

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User( row['name'], row['spending_limit'], row['savings_goal'], row['id'] )
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User( result['name'], result['spending_limit'], result['savings_goal'], result['id'] )
    return user