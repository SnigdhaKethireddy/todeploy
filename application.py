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


dbconn = pymssql.connect(server='databaseadb3.cynlmhdgtwkx.us-east-2.rds.amazonaws.com', port=1433, user='snigdha', password='5190$Niggi', database='adbdatabase')

def largest():
    dbconn = pymssql.connect(server='databaseadb3.cynlmhdgtwkx.us-east-2.rds.amazonaws.com', port=1433, user='snigdha', password='5190$Niggi', database='adbdatabase')
    #dbconn = pymssql.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()


    cursor.execute("select top (5) mag,time,place from all_month order by mag desc")
    rows = cursor.fetchall()
    return render_template('large.html',r=rows)

@application.route("/largest5", methods=['GET'])
def large():
    return largest()

def rad1():
    dbconn = pymssql.connect(server='databaseadb3.cynlmhdgtwkx.us-east-2.rds.amazonaws.com', port=1433, user='snigdha', password='5190$Niggi', database='adbdatabase')
    #dbconn = pymssql.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()


    cursor.execute("Select mag,time,place from all_month where acos(sin((3.14/180)*32.7357) * sin((3.14/180)*latitude) + cos((3.14/180)*32.7357) * cos((3.14/180)*latitude) * cos((3.14/180)*longitude - ((3.14/180)*(-97.1081)))) * 6371 < 500")
    rows = cursor.fetchall()
    return render_template('rad1.html',r=rows)


@application.route("/radi1", methods=['GET'])
def nearer():
    return rad1()


def magni():
    dbconn = pymssql.connect(server='databaseadb3.cynlmhdgtwkx.us-east-2.rds.amazonaws.com', port=1433, user='snigdha', password='5190$Niggi', database='adbdatabase')
    #dbconn = pymssql.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()

    cursor.execute("Select count(*) from all_month where mag>3 and  (TIME between '2020-06-01' and '2020-06-08')")
    rows = cursor.fetchall()
    return render_template('magnitu.html',r=rows)

@application.route('/magnitude', methods=['GET'])
def mag():
    return magni()  




def ritch(magfrom=None,magto=None):
    dbconn = pymssql.connect(server='databaseadb3.cynlmhdgtwkx.us-east-2.rds.amazonaws.com', port=1433, user='snigdha', password='5190$Niggi', database='adbdatabase')
    #dbconn = pymssql.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()


    cursor.execute("Select count(*) from all_month  where( mag BETWEEN " + magfrom +" AND " + magto + ") AND (TIME between '2020-06-10' and '2020-06-12') ")

    rows = cursor.fetchone()
    return render_template('ritcher.html',r=rows)


@application.route('/ritcher', methods=['GET'])
def rit():
    magfrom = request.args.get('magfrom', '')
    magto = request.args.get('magto', '')
    return ritch(magfrom , magto)	







def new():
    dbconn = pymssql.connect(server='databaseadb3.cynlmhdgtwkx.us-east-2.rds.amazonaws.com', port=1433, user='snigdha', password='5190$Niggi', database='adbdatabase')
    #dbconn = pymssql.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()

    cursor.execute("SELECT count(*) FROM all_month WHERE acos(sin((3.14/180)*32.8) * sin((3.14/180)*latitude) + cos((3.14/180)*32.8) * cos((3.14/180)*latitude) * cos((3.14/180)*longitude - ((3.14/180)*(-96.8)))) * 6371 < 1000" )
    rows = cursor.fetchone()
    cursor.execute("SELECT count(*) FROM all_month WHERE acos(sin((3.14/180)*61) * sin((3.14/180)*latitude) + cos((3.14/180)*61) * cos((3.14/180)*latitude) * cos((3.14/180)*longitude - ((3.14/180)*(-150)))) * 6371 < 1000" )
    rowsa = cursor.fetchone()
    return render_template('bet.html',r=rows,f=rowsa)

@application.route('/newsearch', methods=['GET'])
def newarea():
    return new()


def rad2():
    dbconn = pymssql.connect(server='databaseadb3.cynlmhdgtwkx.us-east-2.rds.amazonaws.com', port=1433, user='snigdha', password='5190$Niggi', database='adbdatabase')
    #dbconn = pymssql.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()


    cursor.execute("Select top(1) mag,time,place from all_month where acos(sin((3.14/180)*32.8) * sin((3.14/180)*latitude) + cos((3.14/180)*32.8) * cos((3.14/180)*latitude) * cos((3.14/180)*longitude - ((3.14/180)*(-96.8)))) * 6371 < 200")
    rows = cursor.fetchall()
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
