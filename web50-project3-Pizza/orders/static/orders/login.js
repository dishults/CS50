function Register() {
    var checkBox = document.querySelector("#defaultCheck1");
    let firstName = document.getElementById("firstName"),
        lastName = document.getElementById("lastName"),
        email = document.getElementById("email");

    if (checkBox.checked == true){
        [firstName, lastName, email].forEach(function(element) {
            element.style.display = "initial";
            element.required = true;
        });

    } else {
        [firstName, lastName, email].forEach(function(element) {
            element.style.display = "none";
            element.required = false;
        });
    }
}