from flask import Flask, render_template, redirect, request
from flask import Blueprint
from ..models.category import Category
from ..repositories import category_repository as category_repository

categorys_blueprint = Blueprint("categorys", __name__)

@categorys_blueprint.route("/categorys")
def categorys():
    categorys = category_repository.select_all()
    return render_template("categorys/index.html", categorys=categorys)

@categorys_blueprint.route("/categorys/new", methods=['GET'])
def new_category():
    return render_template("categorys/new.html")

@categorys_blueprint.route("/categorys", methods=['POST'])
def create_category():
    name = request.form['name']
    category = Category(name)
    category_repository.save(category)
    return redirect("/categorys")

@categorys_blueprint.route("/categorys/<id>", methods=['GET'])
def show_category(id):
    category = category_repository.select(id)
    return render_template("categorys/show.html", category=category)

@categorys_blueprint.route("/categorys/<id>/edit", methods=['GET'])
def edit_category(id):
    category = category_repository.select(id)
    return render_template("categorys/edit.html", category=category)

@categorys_blueprint.route("/categorys/<id>", methods=['POST'])
def update_category(id):
    name = request.form['name']
    activated = request.form['activated']
    category = Category(name, activated, id)
    category_repository.update(category)
    return redirect("/categorys")

@categorys_blueprint.route("/categorys/<id>/delete", methods=['POST'])
def delete_category(id):
    category_repository.delete(id)
    return redirect("/categorys")