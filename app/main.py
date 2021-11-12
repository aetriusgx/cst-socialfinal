from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from PIL import Image
from src import users
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

user_data = users.mockup_users

@app.route('/')
def homePage():
	return render_template('home.html')

@app.route('/view_profiles', methods=['POST'])
def view_profiles():
	user = request.form.get('search-user')
	return render_template('profile.html', user=user, user_data=user_data)
