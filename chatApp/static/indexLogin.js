document.addEventListener("DOMContentLoaded", (event) => {
    const sio = io();
    var errorMessagesDiv = document.getElementById("errorMessages");
    var form = document.getElementById("form");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const values = Array.from(formData.values());
        console.log(values);
        const hasEmpty = values.some(value => value.trim() === "");
        console.log(hasEmpty); // true = něco je prázdné

        if (hasEmpty) {
            createErrorMessage("Prosím, vyplňte všechna pole.");
        } else {
            sio.emit("checkLogin", values);
        }

    });


    sio.on("wrongLoginError", () => {
        createErrorMessage("Nepsrávné přihlašovaní údaje.");

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

    sio.on("redirectToMenu", (data) => {
        window.location.href = "/chatRooms/"+data.username;
    });
});