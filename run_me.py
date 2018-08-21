"""
Our drum machine code.
This python file runs the whole system.
The system contains a javascript module that builds the interface
The system runs python as its underlying algorithm
To run this, you need to install flask.
Flask bridges javascript and python. (It uses jinja language), see http://flask.pocoo.org/
In javascript, we display audio wavefile using wavesurfer-js at https://wavesurfer-js.org/
We may use different way to encode data, for example: the "panda" python module
"""


# import the underlying python algorithm that does the calculation
import crazy_drummer

# for using flask
from flask import Flask, render_template, request, jsonify
from flask import redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

# some basic python library
import os
import pandas as pd
import numpy as np


# Some global variable
app = Flask(__name__)
midi_dir = 'static/midi'      # this is the local directory that stores our midi files, if any
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'mid'])   # this is allowed extension of the music files


"""
This is the main function.
It renders a template that stores under template/index.html
It calls a function in receiver/lets_talk that let javascript and python talks
The html (footer.html) loads our javascript functions to help handle the interaction on the web page
For more detail about the interaction of selection, see static/js/byexample.js
"""

@app.route('/')  #interface
def index():
    # grab the static resources
    # pass in the variables and render the template
    return render_template('index.html')


# This is the route that let python and javascrip talk
@app.route('/receiver/lets_talk', methods=['POST'])
def process_talk():
    # get the data from the web interface
    data = request.get_json()
    initial_pattern_number = 12345
    # let python process the data
    crazy_drummer.get_drum_pattern(data,initial_pattern_number)

    return jsonify({
        "status": "done",
        "data": data,
        "pattern_number": initial_pattern_number,
        })


"""
The 'main' function
"""
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host = '127.0.0.1', debug=True)
