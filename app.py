from flask import Flask, request, render_template, redirect, url_for, session, make_response, session
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

import urllib.parse

from forms import RegisterForm, LoginForm
from database.database import *


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "asdf7878"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User(1, "Tobi", "Zillmann", "tobi83301@gmail.com")  # get this data from database


class User(UserMixin):
    def __init__(self, user_id, firstname, lastname, email):
        self.id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


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


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print("asfsdfasdfsaf")
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        phone = form.phone.data
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        street = form.street.data
        house_number = form.house_number.data
        postal_code = form.postal_code.data
        city = form.city.data
        country = form.country.data
        state = form.state.data

        address_id = add_new_address(street, house_number, postal_code, city, country, state)
        add_new_customer(firstname, lastname, email, hashed_password, phone, address_id)

        print((firstname, lastname, email, phone, hashed_password, street, house_number, postal_code, city, country, state))
        return redirect(url_for("home"))

    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    next_page = request.args.get('next')
    if form.validate_on_submit():
        # check if user exists in db https://youtu.be/71EU8gnZqZQ?t=1615
        user = User(1, "Tobi", "Zillmann", "tobi83301@gmail.com")  # get this from db
        session['logged_in'] = True
        session['email'] = user.email
        login_user(user)
        if next_page is not None:
            return redirect(url_for(next_page[1:]))
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    session['logged_in'] = False
    session.pop('email', None)
    logout_user()
    return redirect(url_for("home"))


@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html")


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