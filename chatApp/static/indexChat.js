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

    var users = document.getElementById("usersInRoom").children;
    for (let i = 0; i < users.length; i++){
        var user = users[i].children;
        if (user[1]) {
            user[1].onclick = function(){kickFromRoom(this)};
        }
    }


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

    sio.on("showAddedUser", (data) => {
        var usersInRoomDiv = document.getElementById("usersInRoom");
        var userDiv = document.createElement("div");
        userDiv.id = "userInRoom";
        userDiv.classList.add("userInRoom");
        var addedUser = document.createElement("p");
        var kickButton = document.createElement("button");
        kickButton.onclick = function(){kickFromRoom(this)};
        kickButton.textContent = "Kick";
        addedUser.textContent = data.userName;
        userDiv.appendChild(addedUser);
        userDiv.appendChild(kickButton);
        usersInRoomDiv.appendChild(userDiv);
    });

    sio.on("showUserThatLeft", (data) => {
        var usersInRoom = document.getElementById("usersInRoom");
        for (let i = 1; i < usersInRoom.children.length; i++){ 
            console.log(usersInRoom.children[i]);
            if (usersInRoom.children[i].textContent == data.userName) {
                usersInRoom.children[i].remove();
            }
        };
    });

    sio.on("redirectToTheMenu", (data) => {
        window.location.href = "/chatRooms/"+data.userName;
    });

    function kickFromRoom(kick) {
        var kickParent = kick.parentElement;
        var userToKick = kickParent.children[0].textContent;
        //sio.emit("leaveRoom", roomId.textContent);
        //leaveParent.remove();
        sio.emit("kickUser", userToKick);
        kickParent.remove();
    };
});