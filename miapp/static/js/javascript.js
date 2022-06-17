function deletePortfolio(register_number){
    let text = "Are you sure to delete this register?";
    let number = register_number;

    if (confirm(text) == true){
        text = "The register selected is: "+number;
    }else{
        text = "You pressed Cancel";
    }
    document.getElementById("demo").innerHTML = text;
}