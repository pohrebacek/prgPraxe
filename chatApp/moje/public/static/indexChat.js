document.addEventListener("DOMContentLoaded", (event) => {
    const sio = io();
    var userId = null;
    var input = document.getElementById("input");
    var form = document.getElementById("form");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        if (input.value){
            sio.emit("message", input.value);
            input.value = "";
        }
    });

    sio.on("message", (data) => {
        var item = document.createElement("li");
        item.textContent = data.text;
        if (data.user_id == userId){
            item.style.color = "red";
        }
        document.getElementById("messages").appendChild(item);
        console.log("pico");
    });

});