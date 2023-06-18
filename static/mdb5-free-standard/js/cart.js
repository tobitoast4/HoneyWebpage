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




function updateAmountOfProduct(packung_id, element_changed, element_to_update, single_price) {

    var new_amount = document.getElementById(element_changed).value;
    new_amount = parseInt(new_amount);
    var element = document.getElementById(element_to_update);
    element.innerHTML = ((new_amount * single_price).toFixed(2)).replace(".", ",");

    var cart_cookie = JSON.parse(getCookie("cart_cookie"));
    cart_cookie[packung_id] = new_amount;

    document.cookie = "cart_cookie=" + JSON.stringify(cart_cookie) + "; path=/";

    updateTotalPrice();
    setTotalAmountOfProductsInCart();
}


// Löscht Produkt aus Warenkorb aus cart_cookie und aus der Seite selbst
// Gibt daraufhin ein Notify darüber aus
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


// Funktion setzt Gesamtpreis im Warenkorb neu
// Wird aufgerufen, sobald Anzahl einer Reihe (-> eines Produktes) aktualisiert wird
function updateTotalPrice() {
    var all_price_elements = document.querySelectorAll('*[id^="price"]');
    var sum = 5;

    for (var i = 0; i < all_price_elements.length; i++) {
        sum = sum + parseFloat((all_price_elements[i].innerHTML).replace(",", "."));
    }

    sum_total = sum.toFixed(2) + " EUR";
    sum_total = sum_total.replace(".", ",");

    document.getElementById("total_price").innerHTML = sum_total;

    sum_mwst = sum * 0.19;
    sum_mwst = sum_mwst.toFixed(2) + " EUR";
    sum_mwst = sum_mwst.replace(".", ",");

    document.getElementById("mwst_price").innerHTML = sum_mwst;
}


//setzt Anzahl der Produkte im Warenkorb bei Seitenaufruf
setTotalAmountOfProductsInCart();

