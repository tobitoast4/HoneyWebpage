function addProductToCart(product_id, product_count) {

    var product_name = "PRODUCT_TEST"
    var notifyPName = product_name;
    if (product_count != 1) notifyPName = "(" + product_count + "x) " + product_name;

    new Notify({
        title: unescape("Zu Einkaufswagen hinzugef%FCgt"),
        text: notifyPName,
        effect: 'slide',
        speed: 300,
        status: 'success',
        autoclose: true,
        autotimeout: 3500,
        position: 'right bottom',
        gap: 20,
        distance: 70
    })
    var cart_cookie = JSON.parse(getCookie("cart_cookie"));
    var current_number_of_product = parseInt(cart_cookie[product_id]);

    if (!current_number_of_product) {
        current_number_of_product = 0;
    }

    current_number_of_product = parseInt(current_number_of_product) + parseInt(product_count);
    cart_cookie[product_id] = current_number_of_product;

    document.cookie = "cart_cookie=" + JSON.stringify(cart_cookie) + "; path=/";


    setTotalAmountOfProductsInCart();
}

// Setzt Anzahl der Produkte im Warenkorb (-> rotes Badge in Navbar am Warenkorb-Icon)
function setTotalAmountOfProductsInCart() {
    var product_counter = document.getElementById("product_counter");
    if (getSumOfProductsInCart() <= 0) {
        product_counter.setAttribute("style", "display: none");
    } else {
        product_counter.removeAttribute("style");
        product_counter.innerHTML = getSumOfProductsInCart();
    }
}

function getSumOfProductsInCart() {
    var cart_cookie = JSON.parse(getCookie("cart_cookie"));
    var sum = 0;

    if (cart_cookie != null) {
        Object.keys(cart_cookie).forEach(function (k) {
            sum = sum + cart_cookie[k];
        });
    }
    return sum;
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "{}";
}


function removeCartRow(packung_id, element_to_remove, name) {
    var cart_cookie = JSON.parse(getCookie("cart_cookie"));
    delete cart_cookie[packung_id];
    document.cookie = "cart_cookie=" + JSON.stringify(cart_cookie) + "; path=/";

    document.getElementById(element_to_remove).remove();

    new Notify({
        title: "Aus Einkaufswagen entfernt",
        text: name,
        effect: 'slide',
        speed: 300,
        status: 'warning',
        autoclose: true,
        autotimeout: 3500,
        position: 'right bottom',
        gap: 20,
        distance: 70
    })

    updateTotalPrice();
    setTotalAmountOfProductsInCart();
}

//setzt Anzahl der Produkte im Warenkorb bei Seitenaufruf
setTotalAmountOfProductsInCart();