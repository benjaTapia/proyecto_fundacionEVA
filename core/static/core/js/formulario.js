$("#formulario").validate(
	{
		"rules":
		{
			"montoAporte":
			{
				required: true,
				digits: true,
				min: 500,
			},
			"tarjetaAporte":
			{
				required: true,
				minlength: 16,
				maxlength: 16,
			},
			"fechaAporte":
			{
				required: true,
			},
		},
		messages:
		{
			"montoAporte":
			{
				required: 'Este campo es obligatorio',
				min: 'Debe ser como mínimo $500',
			},
			"tarjetaAporte":
			{
				required: 'Este campo es obligatorio',
				minlength: 'La tarjeta debe contener 16 números',
				maxlength: 'La tarjeta debe contener 16 números',
			},
			"fechaAporte":
			{
				required: 'Debe ingresar la fecha de aporte. la fecha debe ser desde mañana en adelante',
			},
		}
});