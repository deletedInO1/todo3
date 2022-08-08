tasks = [];
var day = new Date().getDay();
color1 = "red";
color2 = "green";
var myBody = document.getElementById("content")
function generateTask(text){
    tasks.push(text);
    let t = document.createElement("div");
    t.classList.add("taskdiv");
    let c = document.createElement("div");
    c.classList.add("check");
    c.addEventListener("click", onCheck)
    t.appendChild(c);
    let s = document.createElement("p");
    s.classList.add("taskname");
    s.innerHTML = text;
    t.appendChild(s);
    r = document.createElement("button");
    r.addEventListener("click", onRemove(text, t));
    r.innerHTML = "löschen";
    t.appendChild(r);
    myBody.appendChild(t);
}
function onCheck(event){
    let style = event.target.style
    if(style.backgroundColor == color2){
        style.backgroundColor = color1;
    } else{
        style.backgroundColor = color2;
    }
}
function generate(mytasks){
    tasks = mytasks;
    while(myBody.firstChild){
        myBody.firstChild.remove();
    }
    i = document.createElement("input");
    //i.value = "wadjiw"
    i.id = "inp";
    myBody.appendChild(i);
    b = document.createElement("button");
    b.id = "inpbutton";
    b.innerHTML = "add";
    b.addEventListener("click", () => {
        t = document.getElementById("inp").value;
        fetch(window.location.href, {
            method: "POST",
            body: JSON.stringify({
                id: tasks.length-1,
                action: "create",
                name: t
            })
        });
    })
    myBody.appendChild(b);
    for(var t in tasks){
        generateTask(tasks[t]);
    }
}
setInterval(() => {
    var day2 = new Date().getDay();
    if(day != day2){
        day = day2;
        fetch("/checklist", {
            method: "POST",
            body: JSON.stringify({
                id: 0,
                action: "reset"
            })
        });
    }
    
}, 1000*60*60);
function removeTask(task, div) {
    let id = tasks.indexOf(task);
    fetch("/checklist", {
        method: "POST",
        body: JSON.stringify({
            id: id,
            action: "remove"
        })
    });
    //tasks = tasks.filter(x => x != task);
    //div.remove();
}
function onRemove(task, div){
    return function(){
        removeTask(task, div)
    }
}
//generateTask("task lul");
//generate();