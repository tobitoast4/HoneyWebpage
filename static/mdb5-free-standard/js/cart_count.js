function addProductToCart(product_id, product_count) {

    console.log(product_id);
    console.log(product_count);

//    new Notify({
//        title: unescape("Zu Einkaufswagen hinzugef%FCgt"),
//        text: notifyPName,
//        effect: 'slide',
//        speed: 300,
//        status: 'success',
//        autoclose: true,
//        autotimeout: 3500,
//        position: 'right bottom',
//        gap: 20,
//        distance: 70
//    })
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
//    var cart_cookie = JSON.parse(getCookie("cart_cookie"));
//    var sum = 0;
//
//    if (cart_cookie != null) {
//        Object.keys(cart_cookie).forEach(function (k) {
//            sum = sum + cart_cookie[k];
//        });
//    }
    return 3;
}

//setzt Anzahl der Produkte im Warenkorb bei Seitenaufruf
setTotalAmountOfProductsInCart();