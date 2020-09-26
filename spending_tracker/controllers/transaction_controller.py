from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", merchants=merchants)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transactions():
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    merchant = merchant_repository.select(request.form['merchant_id'])
    transaction = Transaction(amount, category, date, merchant)
    transaction_repository.save(transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>", methods=['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", transaction=transaction)

@transactions_blueprint.route("/transactions/<id>/edit", methods=['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    all_transactions = transaction_repository.select_all()
    return render_template("transactions/edit.html", transaction=transaction, merchants=merchants, all_transactions=all_transactions)

@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    merchant = request.form['merchant_id']
    merchant = merchant_repository.select(merchant)
    transaction = Transaction(amount, category, date, merchant, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")
