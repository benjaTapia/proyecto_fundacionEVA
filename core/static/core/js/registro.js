$('#registro').validate({
    "rules": {
       "rut": {
            required: true,
       },
       "first_name": {
            required: true,
            minlength: 3,
            maxlength: 150,
       },
       "last_name": {
            required: true,
            minlength: 3,
            maxlength: 150,
       },
       "email": {
            required: true,
            email: true
       },
       "username": {
            required: true
        },
       "password1": {
            required: true,
            minlength: 10
       },
       "password2": {
            required: true,
            equalTo:"#id_password1"
       },
    },
    messages: {
       "rut": {
            required: 'Debe ingresar un RUT válido',
       },
       "last_name": {
            required: "Por favor ingresa tu nombre",
            minlength: "Debe tener mínimo 3 letras"
       },
       "first_name": {
            required: "Por favor ingresa tu apellido",
            minlength: "Debe tener mínimo 3 letras"
       },
       "email": {
            required: 'Debe ingresar su correo electrónico',
            email: 'Formato de correo incorrecto'
       },
       "username": {
            required: 'El usuario es un dato obligatorio'
        },
       "password1": {
            required: "Por favor ingresa una contraseña",
            minlength: "La contraseña debe tener un mínimo de 10 caracteres y una mayúscula."
       },
       "password2": {
            required: "Por favor ingrese su contraseña",
            equalTo: "Ambos datos deben coincidir"
       },
    }
 });
 
 function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
 }
 function validateRut(rutCompleto) {
    if (!/^[0-9]+-[0-9kK]{1}$/.test(rutCompleto))
       return false;
    var tmp = rutCompleto.split('-');
    var rut = tmp[0];
    var digv = tmp[1];
    if (digv == 'k') digv = 'K';
    return (dv(rut) == digv);
 }
 
 function dv(T) {
    var M = 0, S = 1;
    for (; T; T = Math.floor(T / 10))
       S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
 }
 
 $.validator.addMethod(
    "validateemail",
    function (value, element, validate) {
       debugger
       if (validate) {
          return validateEmail(value);
       }
    },
    "Formato de correo incorrecto"
 );
 
 $.validator.addMethod(
    "onenumber",
    function(value, element, validate) {
        if (validate) {
            var re = new RegExp('.*[0-9].*');
            resp = re.test(value);
            return resp;
        }
    },
    "La contraseña debe contener al menos un número"
 );
 
 $.validator.addMethod(
    "onemayus",
    function(value, element, validate) {
        if (validate) {
            var re = new RegExp('.*[A-Z].*');
            resp = re.test(value);
            return resp;
        }
    },
    "La contraseña debe contener al menos una mayúscula"
 );
 
 $.validator.addMethod(
    "rut",
    function(value, element, validate) {
        if (validate) {
            return validateRut(value);
        }
    },
    "El formato del rut no es válido"
 );
 
 $("#rut").rules("add", { rut: true });
 $("#email").rules("add", { validateemail: true });
 $("#password1").rules("add", { onenumber: true });
 $("#password1").rules("add", { onemayus: true });
 
 jQuery.validator.addMethod("Permitido", function(value, element) {
   return this.optional(element) || /^[0-9a-z\-.@+_]+$/i.test(value);
    }, "No puede contener caracteres especiales distintos a: @/./+/-/_");

$("#id_username").rules("add", {Permitido: true});