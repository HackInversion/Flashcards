#main.py
# the import section
import webapp2
import os
import jinja2
import json


from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        main_template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write("test")

=======
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render())

class SignUp(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write("Welcome")

class Profile(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write("Welcome")
>>>>>>> a2fddf538fc8ad030562374f4e0a458a46b0edb9

app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/signup', SignUp),
    # ('/profile', Profile)
], debug=True)
