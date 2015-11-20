from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)
#app.config.from_pyfile('config.py')

@app.route('/save',methods=['GET','POST'])
def databaseupdate():
	#user = {'ip': 'str(request.form)'}
#	f=open("data.txt",w)
#	f.write(str(user['ip']))
#	f.close()
	return request.data
@app.route('/show',methods=['GET'])
def ipdisplay():
	f=open('data.txt',r)
	ip=f.read()
	f.close()
	return ip
if __name__=="__main__":
        app.run(host = '0.0.0.0')
