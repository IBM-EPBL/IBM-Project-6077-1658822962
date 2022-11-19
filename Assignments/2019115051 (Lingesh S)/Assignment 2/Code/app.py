from flask import Flask, render_template, url_for, redirect, flash,session,request

#ibm database
import ibm_db as db

#using flaskforms i have separated all the classes to forms.py inside classes
from classes import forms


#importing configurations
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
conn = db.connect("DATABASE=bludb;HOSTNAME=???;PORT=???;Security=SSL;SSLServerCertificate=/Users/shady/Documents/Projects/x64py/Job recommender/untitled folder/DigiCertGlobalRootCA.crt;UID=???;PWD=???",'','')


@app.route('/login',methods=['GET','POST'])
def login():
	form = forms.login()
	if(request.method == 'POST'):
		uname = request.form['uname']
		pwrd = request.form['pwrd']
		sql = "select * from users where uname=?"
		stmt = db.prepare(conn,sql)
		db.bind_param(stmt,1,uname)
		db.execute(stmt)
		account = db.fetch_assoc(stmt)
		if(account):
			if(account['PWRD'] == pwrd):
				session['NAME'] = account['NAME']
				return redirect(url_for('home'))
			else:
				flash('Incorrect Username or Password')
				return redirect(url_for('login'))
		else:
			redirect(url_for('register'))

	return render_template('login.html',form=form)





@app.route('/home')
def home():
	if("NAME" in session):
		return render_template('home.html',name=session['NAME'])
	else:
		return redirect(url_for('login'))


@app.route('/register',methods=['GET','POST'])
def register():
	form = forms.register()
	if(request.method == 'POST'):
		if(form.validate_on_submit()):
			name = request.form['name']
			uname = request.form['uname']
			pwrd = request.form['pwrd']
			email = request.form['email']
			sql = "insert into users values(?,?,?,?)"
			stmt = db.prepare(conn,sql)
			db.bind_param(stmt,1,name)
			db.bind_param(stmt,2,uname)
			db.bind_param(stmt,3,email)
			db.bind_param(stmt,4,pwrd)
			db.execute(stmt)
			flash('You are successfully registered! You can login now')
			return redirect(url_for('login'))
	return render_template('register.html',form=form)





if(__name__ == '__main__'):
	app.run(host='localhost',port = 3000,debug = True)







