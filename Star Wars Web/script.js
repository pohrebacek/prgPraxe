//document.addEventListener('DOMContentLoaded', function () {
//    var input = document.getElementById('my-select');
//    if (localStorage['my-select']) { // if job is set
//        input.value = localStorage['my-select']; // set the value
//    }
//    input.onchange = function () {
//         localStorage['my-select'] = this.value; // change localStorage on change
//         
//        }
// });
//
//
//
// document.getElementById('my-select').addEventListener("change", function () {
//    var selectedColor = this.options[this.selectedIndex].value;
//    this.style.color = selectedColor;
//});



//function pico() {
//    if (document.getElementById("flag").toggleClass == ".flag"){
//        document.getElementById("flag").toggleClass == ".flag.red"
//    } else {
//        document.getElementById("flag").toggleClass == ".flag"
//    }
//}



//$(".flag").click(function(){
//    $(this).toggleClass("flag.red")  ; 
//   })




var caseKok;
var flag;
var arrow;
var tick;
var stav;
test = "kokot";
var stavParentID;





//console.log("pico");
//console.log(States)
//const States2 = Array.from(States);
//console.log(States2)




/*var States = document.getElementsByClassName("stav");

for (i = 0; i < States.length; i++){
    States[i].setAttribute("id", i);
    console.log(i);
}
var index = 0; // index prvku, který chcete získat
var element = States[index];
console.log(element);*/






var stavClasses = document.querySelectorAll(".stav");
        console.log(stavClasses)
        for (i = 0; i < stavClasses.length; i++){
            stavClasses[i].setAttribute("id", stavClasses[i].children[0].id.substring(5));
            //console.log(stavClasses[i].children[0].id.substring(5));
            //console.log(i);
        }

       const pocetStav = stavClasses.length;
       // 
       // console.log("Počet použitých .stav prvků: " + pocetStav);
       // var test;
       // console.log(test);


var poleSave = new Array(stavClasses.length);
for (i = 0; i < poleSave.length; i++){
    poleSave[i] = stavClasses[i].id;
}
console.log(poleSave)




function flagChange(picoTodle) {
    console.log(picoTodle)
    //var flag = document.getElementById("flag");
    flag = document.getElementById(picoTodle.id);
    

    stavParent = flag.parentNode;
    stavParentID = stavParent.id;
    console.log("ID tohohle stavu: "+stavParentID);
    stav = stavParent.children;
    arrow = stav[1];    //těmahle chujovinama mam oštřený to, že se mi vezme i další element a nespadne to na držku
    tick = stav[2];
    //console.log(flag);

    poleSave[stavParentID] = stavParentID;
    for (i = 0; i < poleSave.length; i++){
        console.log(stavClasses[i].id);
        if (stavClasses[i].id == stavParentID){
            if(flag.classList.contains("flag")){
                caseKok = "flagRed";
                localStorage.setItem(stavClasses[i].id, JSON.stringify(caseKok));
            } else {
                caseKok = "flag";
                localStorage.setItem(stavClasses[i].id, JSON.stringify(caseKok));
            }
        }
    }


    
    
}



function arrowChange(picoTodle) {
    console.log(picoTodle)
    arrow = document.getElementById(picoTodle.id);

    stavParent = arrow.parentNode;
    stavParentID = stavParent.id;
    console.log("ID tohohle stavu: "+stavParentID);
    stav = stavParent.children;
    flag = stav[0];
    tick = stav[2];

    poleSave[stavParentID] = stavParentID;

    caseKok = "arrow";
    for (i = 0; i < poleSave.length; i++){
        if (stavClasses[i].id == stavParentID){
            if(arrow.classList.contains("arrow")){
                caseKok = "arrowBlue";
                localStorage.setItem(stavClasses[i].id, JSON.stringify(caseKok));
            } else {
                caseKok = "arrow";
                localStorage.setItem(stavClasses[i].id, JSON.stringify(caseKok));
            }
        }
    }
}

function tickChange(picoTodle) {
    console.log(picoTodle)
    tick = document.getElementById(picoTodle.id);

    stavParent = tick.parentNode;
    stavParentID = stavParent.id;
    console.log("ID tohohle stavu: "+stavParentID);
    stav = stavParent.children;
    flag = stav[0];
    arrow = stav[1];

    poleSave[stavParentID] = stavParentID;

    caseKok = "tick";
    for (i = 0; i < poleSave.length; i++){
        if (stavClasses[i].id == stavParentID){
            if(tick.classList.contains("tick")){
                caseKok = "tickGreen";
                localStorage.setItem(stavClasses[i].id, JSON.stringify(caseKok));
            } else {
                caseKok = "tick";
                localStorage.setItem(stavClasses[i].id, JSON.stringify(caseKok));
            }
        }
    }

}




setInterval(() => {



    for (i = 0; i < pocetStav; i++){
        
        
        let GetTheme = JSON.parse(localStorage.getItem(stavClasses[i].id));

        //console.log(GetTheme);
        var flag1 = stavClasses[i].children[0];
        var arrow1 = stavClasses[i].children[1];
        var tick1 = stavClasses[i].children[2];
        
        if(GetTheme === "flagRed"){
            flag1.classList.replace("flag", "flagRed");
            arrow1.classList.replace("arrowBlue", "arrow");
            tick1.classList.replace("tickGreen", "tick");
        } else if(GetTheme === "tickGreen"){
            flag1.classList.replace("flagRed", "flag");
            arrow1.classList.replace("arrowBlue", "arrow");
            tick1.classList.replace("tick", "tickGreen");
        } else if(GetTheme === "arrowBlue"){
            flag1.classList.replace("flagRed", "flag");
            arrow1.classList.replace("arrow", "arrowBlue");
            tick1.classList.replace("tickGreen", "tick");
        }
        else {
            flag1.classList.replace("flagRed", "flag");
            arrow1.classList.replace("arrowBlue", "arrow");
            tick1.classList.replace("tickGreen", "tick");
        }

        
    }

    
}, 5);











