from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session


app = Flask(__name__)
Session(app)


@app.route('/')
def home():

    prod = [
        {
            "title": "TANNENHONIG",
            "description": "Kräftiger und flüssiger Honig, der kaum kandiert. Er zeichnet sich durch seinen würzig-kräftigen Geschmack aus!",
            "image_id": 1,
            "quantity": 500,
            "price": "12.50",
        },
        {
            "title": "WALDHONIG",
            "description": "Bei diesem Honig dominiert der Honigtau-Anteil, was ihn zu einem angenehm malzigen, aromatischen Honig macht. Zusätzlich ist noch ein Teil Waldblüte enthalten, der den Honig mit einer feinen Süße abrundet.",
            "image_id": 2,
            "quantity": 500,
            "price": "10.00",
        },
        {
            "title": "SPÄTSOMMERHONIG",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi egestas sapien at augue molestie, sed porta libero faucibus. Vivamus at commodo nibh. Integer vel neque velit. Ut semper sem tellus, eu auctor dui maximus a. Ut a massa non lorem scelerisque dignissim. Curabitur a magna ac dolor convallis dictum fermentum sit amet purus.",
            "image_id": 3,
            "quantity": 500,
            "price": "8.50",
        },
        {
            "title": "BLÜTENHONIG - PERLMUTSCHATZ",
            "description": "Pollenreicher Blütenhonig von Raps und Löwenzahn, schnell kandierend.",
            "image_id": 4,
            "quantity": 500,
            "price": "8.50",
        },
        {
            "title": "BLÜTENHONIG - FRÜHE BLÜTENBEUTE",
            "description": "Pollenreicher Blütenhonig von Raps und Löwenzahn, schnell kandierend.",
            "image_id": 5,
            "quantity": 500,
            "price": "8.50",
        },
        {
            "title": "BLÜTENHONIG - BLÜTEN DER SONNE",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi egestas sapien at augue molestie, sed porta libero faucibus. Vivamus at commodo nibh. Integer vel neque velit. Ut semper sem tellus, eu auctor dui maximus a. Ut a massa non lorem scelerisque dignissim. Curabitur a magna ac dolor convallis dictum fermentum sit amet purus.",
            "image_id": 6,
            "quantity": 500,
            "price": "8.50",
        },
    ]

    return render_template("home.html", products=prod)



@app.route('/product&id=<product_id>')
def product(product_id):
    p = {
        "title": "BLÜTENHONIG - BLÜTEN DER SONNE",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi egestas sapien at augue molestie, sed porta libero faucibus. Vivamus at commodo nibh. Integer vel neque velit. Ut semper sem tellus, eu auctor dui maximus a. Ut a massa non lorem scelerisque dignissim. Curabitur a magna ac dolor convallis dictum fermentum sit amet purus.",
        "image_id": 6,
        "quantity": 500,
        "price": "8.50",
    },
    return render_template("product.html", product=p)


@app.route('/cart')
def cart():

    prod = [
        {
            "title": "TANNENHONIG",
            "description": "Kräftiger und flüssiger Honig, der kaum kandiert. Er zeichnet sich durch seinen würzig-kräftigen Geschmack aus!",
            "image_id": 1,
            "quantity": 500,
            "price": "12.50",
        },
        {
            "title": "WALDHONIG",
            "description": "Bei diesem Honig dominiert der Honigtau-Anteil, was ihn zu einem angenehm malzigen, aromatischen Honig macht. Zusätzlich ist noch ein Teil Waldblüte enthalten, der den Honig mit einer feinen Süße abrundet.",
            "image_id": 2,
            "quantity": 500,
            "price": "10.00",
        }
    ]

    return render_template("cart.html", products=prod)


if __name__ == '__main__':
    # app.run(host="0.0.0.0") # use me for prod
    app.run(host="127.0.0.1", port=5009)