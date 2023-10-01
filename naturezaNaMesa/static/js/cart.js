var updateButtons = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateButtons.length; i++) {
  updateButtons[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "action:", action);

    console.log("USER", user);
    if (user == "AnonymousUser") {
      console.log("Usuário não encontrado");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("O usuário está logado, enviando os dados...");

  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      productId: productId,
      action: action,
    }),
  })
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      console.log("data:", data);
    });
}
