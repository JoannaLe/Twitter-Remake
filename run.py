from __future__ import print_function
from flask import Flask, request, redirect, render_template, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, logout_user
from models import app, db, login, User
from forms import LoginForm, RegistrationForm
import sys

@app.route('/', methods=['GET'])
def home():
	# query all messages
	# msgs = Message.query.all()
	return render_template('base.html')#, messages=msgs)

@app.route('/login/', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect('/')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		print("FORM VALIDATED")
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			print('INVALID')
			return redirect(url_for('login'))
		print('successful credentials')
		login_user(user)
		flash('Logged in successfully.')
		return redirect('/')
	return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect('/')

@app.route('/signup', methods=['GET','POST'])
def signup():
	if current_user.is_authenticated:
		return redirect('/')
	# validate registration info and create new user
	form = RegistrationForm()
	if request.method == 'POST' and form.validate_on_submit():
		new_user = User(username=str(form.username.data))
		new_user.set_password(form.password.data)
		db.session.add(new_user)
		db.session.commit()
		print('registration successful')
		flash('Registration Successful.')
		return redirect(url_for('login'))
	# get request for registration page
	return render_template('register.html', form=form)