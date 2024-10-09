document.addEventListener("DOMContentLoaded", (event) => {
    const sio = io();
    var userId = null;
    var yourId = document.getElementById("yourId");
    var roomForm = document.getElementById("createRoomForm");
    var roomInput = document.getElementById("roomNameInput");
    var chatRooms = document.getElementById("chatRooms");
    var currentUrl = window.location.href;
    console.log(currentUrl);
    if (document.getElementById("rooms")){
        var rooms = chatRooms.children;
        for (let i = 0; i < rooms.length; i++){
            var roomChild = rooms[i].children;
            roomChild[1].onclick = function(){openRoom(this)};
            roomChild[2].onclick = function(){deleteRoom(this)};
        }
    }
    var userName = currentUrl.split("/");
    sio.emit("saveUsername", userName[4]);


    roomForm.addEventListener("submit", (e) => {
        e.preventDefault();
        if (roomInput.value) {
            var newRoom = document.createElement("p");
            newRoom.textContent = roomInput.value;
            var buttonOpen = document.createElement("button"); 
            var buttonDelete = document.createElement("button");  
            buttonOpen.textContent = "Open";        
            buttonDelete.textContent = "Delete";

            buttonDelete.onclick = function(){deleteRoom(this)};
            buttonOpen.onclick = function(){openRoom(this)};
            console.log(buttonDelete);

            var roomsDiv = document.createElement("div");
            roomsDiv.classList.add("rooms");
            chatRooms.appendChild(roomsDiv);
            roomsDiv.appendChild(newRoom);
            roomsDiv.appendChild(buttonOpen);
            roomsDiv.appendChild(buttonDelete);
            
            sio.emit("createRoom", roomInput.value);
            roomInput.value = "";
        }
    });


    function deleteRoom(del) {
        var delParent = del.parentElement;
        roomName = delParent.children[0];
        sio.emit("deleteRoom", roomName.textContent);
        delParent.remove();
    };

    function openRoom(open) {
        console.log("open");
        var openParent = open.parentElement;
        var openRoomName = openParent.children[0];
        window.location.href = "/chat/"+openRoomName.textContent;
    };


    sio.on("connect", () => {
        userId = sio.id;
        console.log(userId);
        yourId.textContent = "your session id: "+userId;
             
    });
});