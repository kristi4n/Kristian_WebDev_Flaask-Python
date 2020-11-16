from flask import Flask, render_template, url_for, request, redirect, session
from app import app
from app.models.user import User ## import kelas User dari model

#@app.route('/', methods = ['GET'])
# def index():
# 	user =  User() ## membuat objek dari kelas user
# 	nama = user.getName() ## memanggil method untuk mengambil nama
# 	return render_template('index.html', nama=nama)

app.secret_key = "Latihan"
authorize = False
currentpage = "index"
@app.route('/')
def index():	
	global currentpage
	currentpage = "index"
	return render_template('index.html')

@app.route('/login', methods = ["GET", "POST"])
def login():		
	error = None
	Data = {
		"username" : "admin",
		"name" : "Administrator",
		"password" : "123" 
	}
	if session:
		return redirect(url_for("index"))
	else:
		if request.method == "POST":
			if Data["username"] == request.form["nama_user"]:
				if Data["password"] == request.form["kata_sandi"]:
					session["username"] = request.form["nama_user"]
					session["name"] = "administrator The Best"
					#return render_template('index.html', session = session)
					return redirect(url_for(currentpage, session = session))
				else:
					error = "Password Salah"
					nama = request.form["nama_user"]
					return render_template('login.html', error = error, nama = nama)
			else:
				error = "Username tidak terdaftar"
				return render_template('login.html', error = error)
		else:
			return render_template('login.html')
			
@app.route('/authenticate')
def authenticate():
	error = None
	Data = {
		"username" : "admin",
		"name" : "Administrator",
		"password" : "123" 
	}
	
	if Data["username"] == request.form["nama_user"]:
		if Data["password"] == request.form["kata_sandi"]:
			return render_template('index.html', session = session)
		else:
			error = "Password Salah"
			return render_template('login.html', error)
	else:
		error = "Username tidak terdaftar"
		return render_template('login.html', error)


@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/logout')
def logout():
	session.pop("username")
	session.pop("name")	
	return redirect(url_for("index"))

@app.route('/useronly')
def useronly():
	global currentpage
	currentpage = "useronly"
	if session:
		return render_template('user_only.html')
	else:
		return redirect(url_for("login"))
		