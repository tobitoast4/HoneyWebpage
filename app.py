from flask import Flask, request, render_template, redirect, url_for, session, make_response, session, flash, get_flashed_messages
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from wtforms.validators import ValidationError

from user import User

import urllib.parse

from forms import RegisterForm, LoginForm, BuyNowForm, BuyForm
from database.database import *


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "asdf7878"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(customer_id):
    print("load_user(email)")
    print(customer_id)
    return get_customer_by_id(customer_id)  # get this data from database


@app.route('/')
def home():
    return redirect(url_for("shop"))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/shop')
def shop():
    order = request.args.get('orderBy', default="newest", type=str)  # newest, oldest, price_asc, price_desc
    search = request.args.get('search', default="", type=str)
    selected_categories = request.args.get('categories', default="", type=str)
    price = request.args.get('price', default="", type=str)

    highest_price = get_highest_product_price()
    min_value = 0
    max_value = highest_price

    if price != "":
        prices = price.split("+")
        min_value = int(prices[0])
        max_value = int(prices[1])

    silder_price_data = {
        "highest_price": highest_price,
        "min_value": min_value,
        "max_value": max_value,
        "min_value_percent": round(min_value / highest_price * 100),
        "max_value_percent": round(max_value / highest_price * 100)
    }

    # finally get the data from the database based on the given url parameters
    products = get_products_filtered(order, min_value, max_value, selected_categories, search)
    categories = get_all_product_categories()

    return render_template("shop.html", products=products, categories=categories, orderBy=order,
                           search=search, selected_categories=selected_categories, silder_price_data=silder_price_data)


@app.route('/product')
def product():
    product_id = request.args.get('id', default=1, type=int)
    p = get_one_product(product_id)
    return render_template("product.html", product=p)


@app.route('/cart', methods=["GET", "POST"])
def cart():
    form = BuyNowForm()
    if form.validate_on_submit():
        return redirect(url_for("buy"))
    resp = make_response(render_template("cart.html", form=form))
    product_data_str = str(get_product_data_for_cart()).replace(" ", "").replace("'", '"')
    resp.set_cookie("product_data", urllib.parse.quote_plus(product_data_str))
    return resp


@app.route('/buy', methods=["GET", "POST"])
@login_required
def buy():
    form = BuyForm()
    if form.validate_on_submit():
        return redirect(url_for("order_finished"))
    resp = make_response(render_template("buy.html", form=form))
    product_data_str = str(get_product_data_for_cart()).replace(" ", "").replace("'", '"')
    resp.set_cookie("product_data", urllib.parse.quote_plus(product_data_str))
    return resp


@app.route('/order_finished')
@login_required
def order_finished():
    return render_template("order_finished.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        if get_customer_by_email(email) is not None:
            flash(f"The email '{email}' is already in use. Please choose another one.")
            return redirect(url_for("register"))
        phone = form.phone.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        street = form.street.data
        house_number = form.house_number.data
        postal_code = form.postal_code.data
        city = form.city.data
        country = form.country.data
        state = form.state.data

        address_id = add_new_address(street, house_number, postal_code, city, country, state)
        add_new_customer(firstname, lastname, email, hashed_password, phone, address_id)

        flash("Sie haben sich erfolgreich registriert! Sie können sich jetzt anmelden.")
        return redirect(url_for("home"))

    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    next_page = request.args.get('next')
    if "user_id" in session:
        return redirect(url_for("home"))
    if form.validate_on_submit():
        # check if user exists in db https://youtu.be/71EU8gnZqZQ?t=1615
        email = form.email.data
        user = get_customer_by_email(email)
        if user is None:
            flash(f"User with email address '{email}' does not exist.")
            return redirect(url_for("login"))
        if not bcrypt.check_password_hash(user.password, form.password.data):
            flash(f"The entered password is not correct.")
            return redirect(url_for("login"))
        session['logged_in'] = True
        session['user_id'] = user.id
        session['email'] = user.email_address
        login_user(user)
        if next_page is not None:
            return redirect(url_for(next_page[1:]))
        flash(f"Sie haben sich erfolgreich eingeloggt!")
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET"])
def logout():
    session['logged_in'] = False
    session.pop('user_id', None)
    session.pop('email', None)
    logout_user()

    return redirect(url_for("home"))


@app.route('/profile')
@login_required
def profile():
    user = get_customer_by_id(session['user_id'])
    address = get_address_by_id(user.default_address_id)
    return render_template("profile.html", user=user, address=address)


@app.route('/orders')
@login_required
def orders():
    return render_template("orders.html")


@app.route('/settings')
@login_required
def settings():
    return render_template("settings.html")


if __name__ == '__main__':
    # app.run(host="0.0.0.0") # use me for prod
    app.run(host="127.0.0.1", port=5009, debug=True)