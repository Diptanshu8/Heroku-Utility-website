from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)
#app.config.from_pyfile('config.py')

@app.route('/',methods=['GET','POST'])
def hello():
	user = {'ip': 'str(request.form)'}
	return render_template('base.html',
                           title='Home',
                           user=user)	
if __name__=="__main__":
        app.run(host = '0.0.0.0')
