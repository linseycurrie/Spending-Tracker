from db.run_sql import run_sql
from models.category import Category

def save(category):
    sql = "INSERT INTO categorys (name, activated) VALUES ( %s, %s ) RETURNING *"
    values = [category.name, category.activated]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category

def select_all():
    categorys =[]

    sql = "SELECT * FROM categorys"
    results = run_sql(sql)

    for row in results:
        category = Category( row['name'], row['activated'], row['id'] )
        categorys.append(category)
    return categorys

def select(id):
    category = None
    sql = "SELECT * FROM categorys WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        category = Category( result['name'], result['activated'], result['id'] )
    return category

def update(category):
    sql = "UPDATE categorys SET (name, activated) = ( %s, %s ) WHERE id = %s"
    values = [category.name, category.activated, category.id]
    print(values)
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM categorys WHERE id = %s"
    values = [id]
    run_sql(sql, values)
