import cgi
import datetime
import wsgiref.handlers
from google.appengine.ext import db

from google.appengine.api import xmpp
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from datetime import datetime, timedelta

import main

class Greeting(db.Model):
  author = db.StringProperty(multiline=True)
  content = db.StringProperty(multiline=True)
  time = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)


ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
def now():
  return datetime.utcnow() + timedelta(hours=+8)
TIME_MSG = now().strftime(ISOTIMEFORMAT)
time = TIME_MSG

maila='hm00com@gmail.com'
mailb='xxx@xxx.com'

class XMPPHandler(webapp.RequestHandler):
  def post(self):
    message = xmpp.Message(self.request.POST)
    BODYMSG = message.body
    def posta():
      global body
      global taga
      
      if maila == message.sender:
          taga = "#miaomiao"
      elif mailb == message.sender:
          taga = "#xxx"
      else:
          taga = " #gaenotes "
      body = message.body
      greeting = Greeting()
      greeting.time = time
      greeting.author = taga
      greeting.content = body
      greeting.put()
    posta()

    REPLY_MSG = BODYMSG + taga + TIME_MSG
    message.reply(REPLY_MSG)

application = webapp.WSGIApplication([('/_ah/xmpp/message/chat/', XMPPHandler)])

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
