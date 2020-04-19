function changeText(){
    var ele = document.getElementById("bId");
    if(ele.value === 'View')
    {
        ele.value = 'Close';
    }
    else
    {
        ele.value = 'View';
    }
    var e = document.getElementById("0");
    console.log(e.value)
    alert(e.value)
    
}