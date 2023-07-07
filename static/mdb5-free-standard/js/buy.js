function fillFinishStepDeliveryAddress(){
    let is_alt_delivery_address_selected = document.getElementById('use_alt_delivery_address').value == "true";
    console.log(is_alt_delivery_address_selected);
    let div_element = document.getElementById("finish_step_delivery_address");

    let div_content = "";
    if(is_alt_delivery_address_selected){
        div_content = div_content + document.getElementById("alt_address_firstname").value + " " + document.getElementById("alt_address_lastname").value;
        div_content = div_content + "<br/>";
        div_content = div_content + document.getElementById("alt_address_street").value + " " + document.getElementById("alt_address_house_number").value;
        div_content = div_content + "<br/>";
        div_content = div_content + document.getElementById("alt_address_postal_code").value + " " + document.getElementById("alt_address_city").value;
        div_content = div_content + "<br/>";
        div_content = div_content + document.getElementById("alt_address_country").value;
        div_content = div_content + "<br/>";
        div_content = div_content + document.getElementById("alt_address_state").value;
        div_content = div_content + "<br/>";
        div_content = div_content + "<br/>";
        div_content = div_content + document.getElementById("alt_address_email").value;
        div_content = div_content + "<br/>";
        div_content = div_content + document.getElementById("alt_address_phone").value;
    } else {
        div_content = "<i>Gleich wie Rechnungsadresse.</i>";
    }

    div_element.innerHTML = div_content;
}

function setSelectedProducts(){
    var product_data = JSON.parse(getCookie("product_data"));
    var cart_cookie = JSON.parse(getCookie("cart_cookie"));

    for (var product_id in cart_cookie) {

        var product_name = "";
        var single_price = -1;
        var amount = cart_cookie[product_id];

        for (var p in product_data) {
            if (product_id == product_data[p]["product_id"]) {
                product_name = product_data[p]["name"];
                single_price = product_data[p]["price"];
            }
        }

        var product_element = `
            <div class="row">
                <div class="col-lg-8 col-sm-9 col-8">
                    <div class="row">
                        <div class="col-lg-2 col-3 d-md-block d-none">
                            <a href="/product?id=` + product_id + `">
                                <img src="static/img/` + product_id + `.webp" height="60px" />
                            </a>
                        </div>
                        <div class="col-lg-10 col-md-9 col-12 d-flex align-items-center">
                            <h6 class="orders-product-name">` + product_name + `</h6>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-sm-1 col-2 d-flex align-items-center">
                    <h6 class="orders-product-price">` + amount + `</h6>
                </div>
                <div class="col-lg-2 col-sm-2 col-2 d-flex align-items-center justify-content-end">
                    <h6 class="orders-product-price">` + ((amount * single_price).toFixed(2)).replace(".", ",") + `</h6>
                </div>
            </div>
        `;

        var htmlObject = document.createElement('li');
        htmlObject.setAttribute("class", "list-group-item");
        htmlObject.setAttribute("style", "padding: 5px 1% 5px 1%");
        htmlObject.innerHTML = product_element;

        document.getElementById('list_of_elements_in_buy').appendChild(htmlObject);
    }
}


fillFinishStepDeliveryAddress();
setSelectedProducts();