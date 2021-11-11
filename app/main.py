from flask import Flask, render_template
from flask_bootstrap import Bootstrap, url_for
from PIL import Image
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def homePage():
	return render_template('home.html')