from flask import Flask
from flask import render_template #renderiza nuestras plantillas html
from flask import request 
from flask_wtf import CsrfProtect #nos protege de ataques csrf
from flask import make_response #nos permite crear cookie
from flask import session #no permite crear secciones

from model import db
from model import User
from flask import g
from flask import flash
from flask import redirect #nos permite redireccionarnos a otra seccion
from flask import url_for #nos regresa la ruta del recurso de algun parametro
import forms
import json
from flask_wtf.csrf import CsrfProtect




from config import DevelomentConfig

app = Flask(__name__)
app.config.from_object(DevelomentConfig)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

@app.route('/', methods = ['GET','POST'])
@app.route('/index')
def index( ):
  
    if 'Email' in session:
        Email = session['Email']
        succes_menssage = 'Se ha iniciado correctamente'
        flash(succes_menssage)
        print(Email)
     
    title = 'Gamework'
    comment_form = forms.formulario(request.form)
    
    return render_template('index.html',title = title, form = comment_form)

@app.route('/sub', methods = ['GET','POST'])
def sub():

	title = "Gamework"
	comment_form = forms.formulario(request.form)
	if request.method == 'POST'and comment_form.validate():
		user = User(comment_form.username.data, 
              		comment_form.email.data, 
              		comment_form.password.data)
		
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))
  
	return render_template('index copy.html', title = title, form = comment_form )

@app.route('/login', methods = ['GET','POST'])
def login():

	login_form = forms.logger(request.form)
	title = 'Gamework'
	#imprimira los datos en la consola si el metodos es post y los datos son validos
	if request.method == 'POST' and login_form.validate():

		email = login_form.email.data
		print(email)
		password = login_form.password.data
		 
		user = User.query.filter_by(email = email).first()

		if user is not None and user.verify_password(password):
			succes_menssage = 'Se ha iniciado correctamente {}'.format(email)
			
			flash(succes_menssage)
			session['Email'] = email
			return redirect( url_for('index') )
   
		else:
			error_menssage = 'Contrase;a no valida'
			flash(error_menssage)
				
	return render_template('logger_user.html', title = title, form = login_form)

@app.route('/cookie')
def cookie():
	reponse = make_response(render_template('cookie.html'))
	reponse.set_cookie('sampon','eduardo', samsite='LAX', secure = True)
	return reponse

@app.route('/logout')
def logout():
	if 'Email' in session:
		session.pop('Email')
	return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):

	return render_template('404.html')

@app.route('/ajax-login', methods=['POST'])
def ajax_login():
	print(request.form)
	Email =  request.form['email']
	response = {'status':200, 'Email': Email, 'id':1}

 
	return  json.dumps(response)

@app.route('/home')
def home():
 
    


    return 'Hola mundo'
if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)
	
	with app.app_context():
		db.create_all()
    
	app.run(host='0.0.0.0')