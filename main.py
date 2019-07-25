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
        template = JINJA_ENVIRONMENT.get_template('home.html')

        self.response.write(template.render())
    def post(self):
        response = self.request.get('difficulty_selection')







# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
