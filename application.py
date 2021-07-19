import os
from flask import Flask,redirect,render_template,request
import pymssql
import time
import random
import urllib
import datetime
import json
import pickle
import hashlib

application = Flask(__name__)


@application.route("/")
def index():
   return render_template('index.html')

 
@application.errorhandler(404)
@application.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')


@application.errorhandler(500)
@application.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')

if __name__ == "__main__":
	application.run()
