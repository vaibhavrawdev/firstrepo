function validateForm(){
    var x = document.getElementById('pnumber').value;
    if(isNaN(x) || x ==""){
        alert("Enter valid details!");
        return false;
    }    
}

window.onload = function() 
{
	var submitBtn = document.getElementById('subbutton');
	submitBtn.addEventListener("click", validateForm);
}
