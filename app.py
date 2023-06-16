from flask import Flask, request, render_template, redirect, url_for, session, make_response, session

import urllib.parse

from database.database import *


app = Flask(__name__)
app.config["SECRET_KEY"] = "asdf7878"


@app.route('/')
def home():
    products = get_all_products()
    return render_template("home.html", products=products)


@app.route('/product&id=<product_id>')
def product(product_id):
    p = get_one_product(product_id)
    return render_template("product.html", product=p)


@app.route('/cart')
def cart():
    resp = make_response(render_template("cart.html"))
    product_data_str = str(get_product_data_for_cart()).replace(" ", "").replace("'", '"')
    resp.set_cookie("product_data", urllib.parse.quote_plus(product_data_str))
    return resp


if __name__ == '__main__':
    # app.run(host="0.0.0.0") # use me for prod
    app.run(host="127.0.0.1", port=5009, debug=True)