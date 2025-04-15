document.addEventListener("DOMContentLoaded", (event) => {
    const sio = io();
    var errorMessagesDiv = document.getElementById("errorMessages");
    var form = document.getElementById("form");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        const values = Array.from(formData.values());
        const response = await fetch("/login", {
            method: "POST",
            body: formData
        });
        console.log(values);
        const hasEmpty = values.some(value => value.trim() === "");
        console.log(hasEmpty); // true = něco je prázdné

        if (hasEmpty) {
            createErrorMessage("Prosím, vyplňte všechna pole.");
            return;
        } 
        
        if (!response.ok) {
            createErrorMessage(await response.text());
        } else {
            window.location.href = "/chatRooms/"+values[0];
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