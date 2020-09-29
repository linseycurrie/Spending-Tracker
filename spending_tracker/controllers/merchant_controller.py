from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository



merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants/new", methods=['GET'])
def new_merchant():
    return render_template("merchants/new.html")

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    name = request.form['name']
    location = request.form['location']
    merchant = Merchant(name, location)
    merchant_repository.save(merchant)
    return redirect('/merchants')

@merchants_blueprint.route("/merchants/<id>", methods=['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/show.html", merchant = merchant)

@merchants_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)

@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['name']
    location = request.form['location']
    activated = request.form['activated']
    merchant = Merchant(name, location, activated, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")