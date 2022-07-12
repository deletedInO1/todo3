tasks = [];
var day = new Date().getDay();
color1 = "red";
color2 = "green";
function generateTask(text){
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
    r.addEventListener("click", onRemove(text, t))
    r.innerHTML = "löschen";
    t.appendChild(r);
    document.body.appendChild(t);
}
function onCheck(event){
    let style = event.target.style
    if(style.backgroundColor == color2){
        style.backgroundColor = color1;
    } else{
        style.backgroundColor = color2;
    }
}
function generate(){
    while(document.body.firstChild){
        document.body.firstChild.remove();
    }
    i = document.createElement("input");
    //i.value = "wadjiw"
    i.id = "inp";
    document.body.appendChild(i);
    b = document.createElement("button");
    b.id = "inpbutton";
    b.innerHTML = "add";
    b.addEventListener("click", () => {
        t = document.getElementById("inp").value;
        tasks.push(t);
        generateTask(t);
    })
    document.body.appendChild(b);
    for(var t in tasks){
        generateTask(tasks[t]);
    }
}
setInterval(() => {
    var day2 = new Date().getDay();
    if(day != day2){
        day = day2;
    }
}, 1000*60*60);
function onRemove(task, div){
    return function(){
        tasks = tasks.filter(x => x != task);
        div.remove();
    }
}
//generateTask("task lul");
generate();