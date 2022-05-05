function setCar() {
    var img = document.getElementById("image");
    img.src = this.value;
    return false;
}

document.getElementById("NbaList").onchange = setCar;

//another

function setCartwo() {
    var img = document.getElementById("image_two");
    img.src = this.value;
    return false;
}

document.getElementById("NbaList_two").onchange = setCartwo;

