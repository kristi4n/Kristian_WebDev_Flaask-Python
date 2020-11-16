from flask import Flask, render_template, url_for, request, redirect
from app import app
from app.models.user import User ## import kelas User dari model

#@app.route('/', methods = ['GET'])
# def index():
# 	user =  User() ## membuat objek dari kelas user
# 	nama = user.getName() ## memanggil method untuk mengambil nama
# 	return render_template('index.html', nama=nama)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login2', methods = ["GET", "POST"])
def login():
	if request.method == "POST":		
		return redirect(url_for("index"))
	else:
		return render_template('login.html')

@app.route('/register2')
def register():
	return render_template('register.html')