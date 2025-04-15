document.addEventListener("DOMContentLoaded", (event) => {
    const sio = io();
    var errorMessagesDiv = document.getElementById("errorMessages");
    var form = document.getElementById("registerForm");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const values = Array.from(formData.values());
        console.log(values);
        const hasEmpty = values.some(value => value.trim() === "");
        console.log(hasEmpty); // true = něco je prázdné

        if (hasEmpty) {
            createErrorMessage("Prosím, vyplňte všechna pole.");
        } else if (values[1] != values[2]) {
            createErrorMessage("Vámi zadaná hesla musí být stejná.");
        } else {
            sio.emit("checkRegisterUserName", values);
        }

    });

    function createErrorMessage(msg) {
        if (!document.getElementById("errorMsg")) {
            let errorMsg = document.createElement("p");
            errorMsg.id = "errorMsg";
            errorMsg.textContent = msg;
            errorMessagesDiv.appendChild(errorMsg);
        } else {
            let errorMsg = document.getElementById("errorMsg");
            errorMsg.textContent = msg;
        }
    };

    sio.on("sameUserNameError", () => {
        createErrorMessage("Vámi zadané jméno je už zabrané");

    });

    sio.on("redirectToMenu", (data) => {
        window.location.href = "/chatRooms/"+data.username;
    });
});