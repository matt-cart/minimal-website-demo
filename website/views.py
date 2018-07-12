from flask import render_template

from website import app

@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/<name>')
def print_name(name):
	return name