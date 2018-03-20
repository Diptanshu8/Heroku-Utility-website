from flask import Flask
from flask import request
from flask import render_template
import os
import sys
import word_of_the_day.word as word

app = Flask(__name__)

#function to save the IP address of my raspi
@app.route('/save_ip',methods=['GET','POST'])
def databaseupdate():
	f=open("ip.txt",'w')
	f.write(str(request.data))
	f.close()
	return request.data

#function to retrieve the stored IP address of my raspi
@app.route('/show_ip',methods=['GET'])
def ipdisplay():
	f=open('ip.txt','r')
	ip=f.read()
	f.close()
	return ip

#function to show the timetable that is stored on the server.
@app.route('/tt',methods=['GET'])
def timetable_display():
	return render_template('base.html')

#function to show the word of the day, its meaning and citations.
@app.route('/word', methods=['GET'])
def word_of_the_day_to_server():
    try:
        w,m,c = word.find_word_of_the_day()
    except Exception as e:
        return e
    return render_template('word.html',word = w, citations=c , meaning = m)

if __name__=="__main__":
        app.debug=True
        app.run(host = '0.0.0.0')
