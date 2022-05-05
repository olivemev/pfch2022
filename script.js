function setViz() {
    var img = document.getElementById("image");
    img.src = this.value;
    return false;
}

document.getElementById("NbaList").onchange = setViz;

//another

function setViztwo() {
    var img = document.getElementById("image_two");
    img.src = this.value;
    return false;
}

document.getElementById("NbaList_two").onchange = setViztwo;

