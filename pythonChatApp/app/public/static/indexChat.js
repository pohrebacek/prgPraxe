document.addEventListener("DOMContentLoaded", (event) => {
    const sio = io();
    var userId = null;
    var input = document.getElementById("input");
    var form = document.getElementById("form");
    var addUserForm = document.getElementById("addUser");
    var addUserInput = document.getElementById("addUserInput");
    var currentUrl = window.location.href;
    console.log(currentUrl);
    var userName = currentUrl.split("/");
    console.log(userName)
    sio.emit("saveUsername", userName[5]);
    sio.emit("saveRoomId", userName[4]);


    form.addEventListener("submit", (e) => {
        e.preventDefault();
        if (input.value){
            sio.emit("message", input.value);
            input.value = "";
        }
    });

    addUserForm.addEventListener("submit", (e) => {
        e.preventDefault();
        if (addUserInput.value){
            if (addUserInput.value == userName[5]) {
                if (!document.getElementById("SameNameError")) {
                    var errorMsg = document.createElement("p");
                    errorMsg.id = "SameNameError";
                    errorMsg.textContent = "Prosím, zadejte jiné jméno než je vaše!"
                    addUserForm.appendChild(errorMsg);
                }
            } else {
                if (document.getElementById("SameNameError")) {
                    var errorMsg = document.getElementById("SameNameError");
                    errorMsg.remove();
                }
                sio.emit("addUser", addUserInput.value);
                addUserInput.value = "";
            }
        }
    });

    sio.on("message", (data) => {
        const messagesContainer = document.getElementById("messages");
        console.log(messagesContainer);
        var sentBy = data.username;
        messagesContainer.append(sentBy + " napsal: ");
        //console.log(data.username);
        var divBruh = document.createElement("div");
        var item = document.createElement("p");
        item.textContent = data.text;
        if (data.user_id == userId){
            item.style.color = "blue";
        }
        divBruh.appendChild(item);
        divBruh.classList.add("messages");
        messagesContainer.appendChild(divBruh);
        console.log("pico");
    });

    sio.on("connect", () => {
        userId = sio.id;
        console.log(userId);
             
    });
});