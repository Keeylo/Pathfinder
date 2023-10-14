from logging.config import dictConfig
from flask import Flask, redirect, request, url_for

import requests

from flask import request
from flask import Flask, render_template

from jinja2 import Template
import secrets

import base64
import json
import os


from flask import session


app = Flask(__name__)

app.secret_key = secrets.token_hex()


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    },
        'file.handler': {
        'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'weatherportal.log',
            'maxBytes': 10000000,
            'backupCount': 5,
            'level': 'DEBUG',
    },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file.handler']
    }
})


@app.route("/")
def index():
    return render_template('index.html')






# Assignment2 TODO: Add route for "/adminlogin"
# This should be the action of the admin form submission
# Use the login() method for reference

# @app.route("/adminlogin", methods=['POST'])
# def admin_login():
#     username = request.form['username'].strip()
#     password = request.form['password'].strip()
#     app.logger.info("Username:%s", username)
#     app.logger.info("Password:%s", password)

#     session['username'] = username

#     my_cities = []

#     my_cities = in_mem_cities

    # return render_template('welcome.html',
    #                        welcome_message="Personal Weather Portal - Admin Portal",
    #                        cities=my_cities,
    #                        name=username,
    #                        addButton_style="display:inline;",
    #                        addCityForm_style="display:inline;",
    #                        regButton_style="display:none;",
    #                        regForm_style="display:none;",
    #                        status_style="display:none;")


if __name__ == "__main__":

    app.debug = False
    app.logger.info('Portal started...')
    app.run(host='0.0.0.0', port=5010)
