#import webapp2
#import jinja2
import os
import datetime
from time import ctime
import urllib2
import json
from flask import Flask,render_template
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/input')
def homepage():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
'''jinja_env=jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    undefined=jinja2.StrictUndefined, #catches template errors
    autoescape=True
)
#http://127.0.0.1:8000/
#To run the code: dev_appserver.py app.yaml
class StartPage(webapp2.RequestHandler): #get, post
    def get(self):
        about_template=jinja_env.get_template('index.html')
        #vars={"username":"Bob"}
        self.response.write(about_template.render())

class InputPage(webapp2.RequestHandler):
    def get(self): #get input
        input_template=jinja_env.get_template('input.html')
        vars={"username":"Bob"}
        self.response.write(input_template.render(vars))
    def post(self): #search
        input_template=jinja_env.get_template('loading.html')
        self.response.write(input_template.render())


app=webapp2.WSGIApplication([
    ('/', StartPage), ('/input', InputPage)
], debug=True)'''
