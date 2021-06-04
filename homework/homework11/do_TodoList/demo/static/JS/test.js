"use strict";

function btOnclick(obj) {
    var flag=obj.value == "Undo"
    if (flag) {
        obj.value = "Done";
    }else{
        obj.value = "Undo";
    }

    function getRowObj(obj) {
        var i = 0;
        while (obj.tagName.toLowerCase() != "tr") {
            obj = obj.parentNode;
            if (obj.tagName.toLowerCase() == "table")
                return null;
        }
        return obj;
    }

    var trObj = getRowObj(obj);
    var trArr = trObj.parentNode.children;
    var trNo;
    for (trNo = 0; trNo < trArr.length; trNo++) {
        if (trObj == trObj.parentNode.children[trNo]) {
            console.log(trNo + 1);
            var x = document.getElementById('test').rows[trNo].cells;
            if(flag)
                x[1].className="DoneContent";
            else
            x[1].className="UndoContent";
        }
    }
}