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

@app.route('/save_link',methods=['GET','POST'])
def linkdatabaseupdate():
	with open("links.csv",'a'):
		w = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		w.writerow(str(request.data))
	return request.data

@app.route('/show_link',methods=['GET'])
def linkdatabaseshow():
	f=open("links.csv",'r')
	links = f.read()
	f.close()
	return links

def data_write(timestamp,link,description):
	with open('data.csv','a') as f:
		fieldnames = ['Time-Stamp','Link','Description']
		writer = csv.DictWriter(f,fieldnames=fieldnames)
		if link == ' ' and timestamp == ' ' and description == ' ': 
			writer.writeheader()
		elif not link == ' ' or not link =='':
			writer.writerow({'Time-Stamp':timestamp,'Link':link,'Description':description})
		else:
@app.route('/temp',methods=['GET'])
def temp():
	f=open('ip.txt','r')
        ip=f.read()
        f.close()
	user={"ip":ip}
	date=ip.split("IST")
	user["date"]=date
	return render_template('base.html',user=user)

if __name__=="__main__":
        app.run(host = '0.0.0.0')
