var updateBtns = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateBtns.length; i++) {

    updateBtns[i].addEventListener("click", function() {

        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log("productId:", productId, "action:", action);
        console.log("USER:", user)

        if (user == 'AnonymousUser') {
            console.log("not user")
        } else {
            updateUserOrder(productId, action)
        }
    })
}
var user = "{{request.user}}"

function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;

}