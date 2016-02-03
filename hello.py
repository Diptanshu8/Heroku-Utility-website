#links is a file to store the links bhai wants to share with me 
from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)
#app.config.from_pyfile('config.py')

@app.route('/save_ip',methods=['GET','POST'])
def databaseupdate():
	#user = {'ip': 'str(request.form)'}
	f=open("ip.txt",'w')
	f.write(str(request.data))
	f.close()
	return request.data
@app.route('/show_ip',methods=['GET'])
def ipdisplay():
	f=open('ip.txt','r')
	ip=f.read()
	f.close()
	return ip

@app.route('/tt',methods=['GET'])
def temp():
	return render_template('base.html')

if __name__=="__main__":
        app.run(host = '0.0.0.0')
