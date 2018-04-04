#!/usr/bin/python3

import json
from flask import Flask
from flask import render_template
from utils import getPlaceDetails

app = Flask(__name__)
with open('config/config.json') as cfile:
    config = json.load(cfile)

with open('config/partners.json') as pfile:
    partners = json.load(cfile)


@app.route('/')
@app.route('/about')
def index():
    return render_template('index.html')


@app.route('/lawncare')
def lawncare():
    return render_template('lawncare.html')


@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')


@app.route('/partners')
def partners():
    return render_template('partners.html')


@app.route('/freequote')
def freequote():
    return render_template('freequote.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', reviews=getPlaceDetails(config.get('placeid'),
                                                                   config.get('apiKey')))


if __name__ == '__main__':
    app.run()
