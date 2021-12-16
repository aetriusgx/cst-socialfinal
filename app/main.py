from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from PIL import Image
from src import users
from random import shuffle

my_username = "developmentuser"

app = Flask(__name__)
bootstrap = Bootstrap(app)
user_data = users.mockup_users

timeline = []
for user in range(0, len(user_data)):
	for post in user_data[user]["posts"]:
		timeline.append([user_data[user]["username"], user_data[user]["posts"][post], user_data[user]["description"]])
shuffle(timeline)

suggested = []
for user in user_data:
	suggested.append([user['username'], user['description']])

@app.route('/',methods=['GET', 'POST'])
def homePage():
	return render_template('home.html', timeline=timeline, user=user_data[0])


@app.route('/view_profiles', methods=['POST'])
def view_profiles():
	user = request.form.get('search-user')
	shuffle(suggested)
	return render_template('profile.html', user=user, user_data=user_data, suggested=suggested)


@app.route('/user/<username>')
def view_user(username):
	userInfo = {}
	count = 0
	likes = 0
	for user in user_data:
		if user['username'] == username:
			user_info = user
			count = len(user['posts'])
			for post in user['posts']:
				likes = likes + user['posts'][post][1]


	
	return render_template('user_profile.html', user_info=user_info, num_posts=count, num_likes=likes)