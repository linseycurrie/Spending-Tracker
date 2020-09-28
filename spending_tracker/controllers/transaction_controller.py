from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import repositories.category_repository as category_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    all_transactions = transaction_repository.select_all()
    total = transaction_repository.total_amount(all_transactions)
    transactions = transaction_repository.sort_transactions(all_transactions)
    categorys = category_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions, total=total, categorys=categorys)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    categorys = category_repository.select_all()
    return render_template("transactions/new.html", merchants=merchants, categorys=categorys)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transactions():
    amount      = request.form['amount']
    category    = category_repository.select(request.form['category_id'])
    date        = request.form['date']
    merchant    = merchant_repository.select(request.form['merchant_id'])
    transaction = Transaction(amount, category, date, merchant)
    transaction_repository.save(transaction)
    return redirect("/transactions")

# @transactions_blueprint.route("/transactions/<id>", methods=['GET'])
# def show_transaction(id):
#     transactions = transaction_repository.select(id)
#     return render_template("transactions/show.html", transactions=transactions)

@transactions_blueprint.route("/transactions/<id>/edit", methods=['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    categorys = category_repository.select_all()
    return render_template("transactions/edit.html", transaction=transaction, merchants=merchants, categorys=categorys)

@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    amount = request.form['amount']
    category = category_repository.select(request.form['category_id'])
    date = request.form['date']
    merchant = merchant_repository.select(request.form['merchant_id'])
    
    transaction = Transaction(amount, category, date, merchant, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/filteredmonth", methods=['POST'])
def filter_month():
    filter = request.form['filter']
    filtered_transactions = transaction_repository.filter_by_month(filter)
    categorys = category_repository.select_all()
    return render_template("transactions/index.html", transactions=filtered_transactions, categorys=categorys)

@transactions_blueprint.route("/transactions/filteredcategory", methods=['POST'])
def filter_category():
    filter = request.form['filter']
    filtered_transactions = transaction_repository.filter_by_category(filter)
    categorys = category_repository.select_all()
    return render_template("transactions/index.html", transactions=filtered_transactions, categorys=categorys)