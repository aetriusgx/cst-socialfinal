from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from PIL import Image
from src import users
from random import shuffle

app = Flask(__name__)
bootstrap = Bootstrap(app)

user_data = users.mockup_users

@app.route('/')
def homePage():
	timeline = []
	for user in range(0, len(user_data)):
		for post in user_data[user]["posts"]:
			timeline.append([user_data[user]["username"], user_data[user]["posts"][post]])
	shuffle(timeline)
	return render_template('home.html', timeline=timeline)


@app.route('/view_profiles', methods=['POST'])
def view_profiles():
	user = request.form.get('search-user')
	return render_template('profile.html', user=user, user_data=user_data)


@app.route('/user/<username>')
def view_user(username):
	userInfo = {}
	for user in user_data:
		if user['username'] == username:
			user_info = user
	
	return render_template('user_profile.html', user_info=user_info)