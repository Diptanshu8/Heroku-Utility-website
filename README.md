# timetable-Heroku
This is a very basic project that I created for adding some ease and mobility to my academic schedule notifier.

#Motivation
Here in IIT Kharagpur, we have to log in to our local system every time to see the schedule of our semester wise classes.
Inorder to avoid this tidious process of logging in everytime, navigating to the location where this timetable is stored and checking it out, I created a mod.
I created a flask repo to which at the beginning of every semseter I provide the screenshots of my timetable and registration card.
I have hosted this project on Heroku<https://www.heroku.com/> and imported this github repository into my heroku app.
This has enabled heroku to host this flask server and given me a static URL that can be accessed from anywhere. Thus I can check my timetable
at any moment of time without needing to have logged into some website.
Another task that I used this is for knowing the IP address of my "Headless-Raspberry Pi". My raspberry pi constantly keeps on polling its IP address on to this server's static URL(RESTful API approach).
Whenever I need to SSH or know the IP of my raspberry pi for some utility, I simple check it out over the link provided by heroku plus my static extension.

#Requirements
1.Python 2.7+
2.flask
3. Heroku account and some basic knowledge of how to host an app on heroku

ENJOY !
