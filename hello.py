from flask import Flask
from flask import request
from flask import render_template
import os
import sys
import random
import word_of_the_day.word as word
import reddit_image_of_the_day.image_downloader as image_downloader

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
    selected_img = random.choice([img for img in os.listdir(os.path.join(os.getcwd(),'static')) if "word_of_day" in img])
    img_path = "../static/"+selected_img
    return render_template('word.html', bg_image = img_path ,word = w, citations = c , meaning = m, citation_count = len(c))

#function to show the reddit image of the day.
@app.route('/iod', methods=['GET'])
def image_of_the_day_viewer():
    args = {'reddit':True}
    result, img_name = image_downloader.download(args)
    if not result:
        return "Some error in downloading the image from reddit."
    img_path = os.path.join('static',img_name)
    return render_template('image_of_the_day_reddit.html', bg_image = img_path )

if __name__=="__main__":
        app.debug=True
        app.run(host = '0.0.0.0')
