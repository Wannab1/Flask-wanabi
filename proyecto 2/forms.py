from wtforms import Form 
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms import HiddenField

from wtforms import validators

def fo_honneypot(form, field):
	if len(field.data) > 0:
		raise validators.ValidationError('El campo debe estar vacio')

class formulario(Form):
	username = StringField('Username',
				[
				validators.Required(message = 'The username is Required'),
				validators.length(min = 4, max =8, message='Entry a username valited')

				]
				)
	email = EmailField('Gmail', 
		[validators.Required('The email is Required'),
		 validators.Email(message='this not is a email valited')
		])
	password = PasswordField('Password',
		[
		validators.Required(message = 'Ingrese su password'),
		validators.length(min = 8, max = 15, message = 'Entry at password')
		]
		)

	honneypot = HiddenField('',[fo_honneypot])

class logger(Form):

	email = EmailField('Email',
		[
		validators.Required(message = 'Ingrese un email valido'),
		validators.Email(message = 'Este no es un email valido')
		]
		)
	password = PasswordField('Password',
		[
		validators.Required(message = 'Ingrese su password'),
		validators.length(min = 8, max = 15, message = 'Entry at password')
		]
		)

