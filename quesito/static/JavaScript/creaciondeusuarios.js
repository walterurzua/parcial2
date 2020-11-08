$(function() {
    //alert('Holaa Mundo en pandemia!!!');
    let numeros = '1234567890-';
    let letras = 'qwertyuiopasdfghjklñzxcvbnm' +
        'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
        'ÁÉÍÓÚáéíóú- ';


    $('.txtrut, .txttelefono ').keypress(function(e) {
        let caracter = String.fromCharCode(e.which);
        if (numeros.indexOf(caracter) < 0)
            return false;
    })
    $('.txtnombre').keypress(function(e) {
        let caracter = String.fromCharCode(e.which);
        if (letras.indexOf(caracter) < 0)
            return false;
    })

    $('.btnEnviar').click(function() {
        let texto = "";
        texto = $('.txtcorreo').val();

        texto = $('.txtcorreo').val();
        if (texto == '') {
            alert('No especificó el correo');
            $('.txtcorreo').focus();
            return;
        }

        if (texto == '') {
            alert('No especificó el rut');
            $('.txtrut').focus();
            return;
        }

        

        if ($('.txtnombre').val() == '') {
            alert('No especificó el nombre por favor intente de nuevo');
            $('.txtnombre').focus();
            return;
        }

        if ($('.txtfecha').val() == '') {
            alert('No especificó la fecha de nacimiento por favor intente de nuevo');
            $('.txtfecha').focus();
            return;
        }

        if ($('.txttelefono').val() == '') {
            alert('No especificó el telefono de contacto por favor intente de nuevo');
            $('.txttelefono').focus();
            return;
        }

        if ($('.txtregion').val() == '0') {
            alert('No especificó la region por favor intente de nuevo');
            return;
        }

        if ($('.txtciudad').val() == '0') {
            alert('No especificó la ciudad por favor intente de nuevo');
            return;
        }

        if ($('.txteducacion').val() == '0') {
            alert('No especificó el nivel de estudio por favor intente de nuevo');
            return;
        }

        alert("Los datos enviados son: \n" +
            $('.txtcorreo').val() + '\n' +
            $('.txtrut').val() + '\n' +
            $('.txtnombre').val() + '\n' +
            $('.txtfecha').val() + '\n' +
            $('.txttelefono').val() + '\n' +
            $('.txtregion').val() + '\n' +
            $('.txtciudad').val() + '\n' +
            $('.txteducacion').val() 
        )
    });

})