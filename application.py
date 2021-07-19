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


def largest():
   

    
    return render_template('large.html',r=rows)

@application.route("/largest5", methods=['GET'])
def large():
    return largest()

def rad1():
    return render_template('rad1.html',r=rows)


@application.route("/radi1", methods=['GET'])
def nearer():
    return rad1()


def magni():
    return render_template('magnitu.html',r=rows)

@application.route('/magnitude', methods=['GET'])
def mag():
    return magni()  




def ritch(magfrom=None,magto=None):
    
    return render_template('ritcher.html',r=rows)


@application.route('/ritcher', methods=['GET'])
def rit():
   
    return ritch(magfrom , magto)	







def new():
    
    return render_template('bet.html',r=rows,f=rowsa)

@application.route('/newsearch', methods=['GET'])
def newarea():
    return new()


def rad2():
    
    return render_template('rad2.html',r=rows)

@application.route('/radi2', methods=['GET'])
def radii():
    return rad2()




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
