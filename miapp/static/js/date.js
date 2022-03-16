'use strict'

window.addEventListener('load', () => {
    console.log('DOM cargado correctamente!');

    function datewithmomentjs(){
        var time = setInterval( () => {
            var span_date = document.querySelector('#date');

            var textHour = moment().format('MMMM Do YYYY, h:mm:ss a');

            span_date.innerHTML = textHour
        }, 500);
        return time;
    }

    try{
        datewithmomentjs();
    }catch(e){
        console.log('Error: '+e);
    }
});