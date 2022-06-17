'use strinct'

$(()=> {
    console.log('The document is ready to work with JQuery');

    $('#portfolio-form-hide').hide();

    $('#portfolio-form-show').click(()=>{
        $('#portfolio-form-show').hide();
        $('#portfolio-form-hide').show();
    });

    $('#save-portfolio').click(()=>{
        $('#portfolio-form-hide').hide();
        $('#portfolio-form-show').show();
    });
});