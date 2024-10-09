var caseKok;
var flag;
var arrow;
var tick;
var stav;
var stavParentID;
var stavClasses = document.querySelectorAll(".stav");

for (i = 0; i < stavClasses.length; i++){
    stavClasses[i].setAttribute("id", stavClasses[i].children[0].id.substring(5));
}

const pocetStav = stavClasses.length;


var poleSave = new Array(stavClasses.length);
for (i = 0; i < poleSave.length; i++){
    poleSave[i] = stavClasses[i].id;
}





function flagChange(justThis) {
    flag = document.getElementById(justThis.id);
    

    stavParent = flag.parentNode;
    stavParentID = stavParent.id;
    stav = stavParent.children;
    arrow = stav[1];
    tick = stav[2];

    poleSave[stavParentID] = stavParentID;
    for (i = 0; i < poleSave.length; i++){
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



function arrowChange(justThis) {
    arrow = document.getElementById(justThis.id);

    stavParent = arrow.parentNode;
    stavParentID = stavParent.id;
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

function tickChange(justThis) {
    tick = document.getElementById(justThis.id);

    stavParent = tick.parentNode;
    stavParentID = stavParent.id;
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



