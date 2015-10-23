from flask import Flask
from flask import request
import os

app = Flask(__name__)
#app.config.from_pyfile('config.py')

@app.route('/',methods=['GET','POST'])
def hello():
	return str(request.data)	
if __name__=="__main__":
        app.run(host = '0.0.0.0')
