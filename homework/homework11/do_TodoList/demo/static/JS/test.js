"use strict";


function getRowObj(obj) {
    var i = 0;
    while (obj.tagName.toLowerCase() != "tr") {
        obj = obj.parentNode;
        if (obj.tagName.toLowerCase() == "table")
            return null;
    }
    return obj;
}

function btDone(obj) {
    var flag=obj.value == "Undo"
    if (flag) {
        obj.value = "Done";
    }else{
        obj.value = "Undo";
    }
    var trObj = getRowObj(obj);
    var trArr = trObj.parentNode.children;
    var trNo;
    for (trNo = 0; trNo < trArr.length; trNo++) {
        if (trObj == trObj.parentNode.children[trNo]) {
            console.log(trNo + 1);
            var x = document.getElementById('mytable').rows[trNo].cells;
            if(flag){
                x[1].className="DoneContent";
                x[2].className="Done";
            }
            else{
                x[1].className="UndoContent";
                x[2].className="Undo";
            }

        }
    }
    states();
}

function btTextToEdit(obj){
    var trObj = getRowObj(obj);
    var trArr = trObj.parentNode.children;
    var trNo;
    for (trNo = 0; trNo < trArr.length; trNo++) {
        if (trObj == trObj.parentNode.children[trNo]) {
            var x = document.getElementById('mytable').rows[trNo].cells;
            console.log(trNo + 1);
            var oldcontent=x[1].innerText;
            var newcontent="<input type='text' class='textedit_update' id='txt_update' placeholder='"+oldcontent+"' onkeypress='return EditKeyPress(this, event)'>";
            x[1].innerHTML=newcontent;
        }
    }
}
function btSearch(){
    var content=document.getElementById('input_search').value;
    if(content==""){
        var len=document.getElementById("mytable").rows.length-1;
        var i=0;
        for(i=1;i<=len;i++){
            var x=document.getElementById("mytable").rows[i];
            x.className="display";
        }
    }else{
        var reg = new RegExp(content,"gi");
        var len=document.getElementById("mytable").rows.length-1;
        var i=0;
        for(i=1;i<=len;i++){
            var x=document.getElementById("mytable").rows[i];
            var isReg = reg.test(x.cells[i].innerText);
            if(!isReg){
                x.className="Notdisplay";
            }
        }
    }
}
function EditKeyPress(obj, e){
    // look for window.event in case event isn't passed in
    e = e || window.event;
    if (e.keyCode == 13)
    {
        var trObj = getRowObj(obj);
        var trArr = trObj.parentNode.children;
        var trNo;
        for (trNo = 0; trNo < trArr.length; trNo++) {
            if (trObj == trObj.parentNode.children[trNo]) {
                console.log(trNo + 1);
                var x = document.getElementById('mytable').rows[trNo].cells;
                x[1].innerHTML=obj.value;
            }
        }
    }
    return true;
}

function delRow(obj){

    var trObj = getRowObj(obj);
    var trArr = trObj.parentNode.children;
    var trNo;
    for (trNo = 0; trNo < trArr.length; trNo++) {
        if (trObj == trObj.parentNode.children[trNo]) {
            console.log(trNo + 1);
            var x = document.getElementById('mytable').rows[trNo].cells;

            var t=document.getElementById("mytable");
            t.deleteRow(trNo);
        }
    }
    states();
}
function addRow(){
    var x=document.getElementById("mytable").rows[1].cells;
    alert([x[1].innerText]);
}
function states(){
    All();
    Done();
    Active();
}
function All(){
    var number=document.getElementById("mytable").rows.length-1;
    var content="All("+number+")";
    document.getElementById("All").innerText=content;
}
function Done(){
    var number=0;
    var len=document.getElementById("mytable").rows.length-1;
    var i=0;
    for(i=1;i<=len;i++){
        var x=document.getElementById("mytable").rows[i].cells;
        if(x[2].className=="Undo")
            number++;
    }
    var content="Done("+number+")";
    document.getElementById("Done").innerText=content;
}
function Active(){
    var number=0;
    var len=document.getElementById("mytable").rows.length-1;
    var i=0;
    for(i=1;i<=len;i++){
        var x=document.getElementById("mytable").rows[i].cells;
        if(x[2].className=="Done")
            number++;
    }
    var content="Active("+number+")";
    document.getElementById("Active").innerText=content;
}
