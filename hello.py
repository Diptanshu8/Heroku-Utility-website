from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)
#app.config.from_pyfile('config.py')

@app.route('/self',methods=['GET','POST'])
def hello():
	ip= str(request.data)
	return render_template('base.html',title='DJ-pi',ip=ip)	
if __name__=="__main__":
        app.run(host = '0.0.0.0')
