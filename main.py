#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi
import datetime
import wsgiref.handlers
from datetime import datetime, timedelta
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp

import xmpp_handler
class Greeting(db.Model):
  author = db.StringProperty(multiline=True)
  content = db.StringProperty(multiline=True)
  time = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

USERA = ['miaomiao','xxx']

def read(self):
    
      self.response.out.write("""
<div id="b3">
<form action="/sign" method="post">
<div id="b31"><textarea name="content"></textarea></div>
<div id="b32"><input type="submit" value="^"></div>
</form>
</div>
<hr align="center" width="100%" size="3" color="#555" style="FILTER: alpha(opacity=100,finishopacity=0,style=3)">
""")
      self.response.out.write("""
<div id="b4">
<table width="100%">
""")
      greetings = Greeting.gql("WHERE author = :author ORDER BY date DESC",
                               author=usertag)
      for greeting in greetings:
          self.response.out.write("""
<tr>
<td>    
<div id="b42">
""")
          
          self.response.out.write("""%s , %s <div id="b41"><tr><td><div id="b41"> %s""" %
                                    (greeting.author, greeting.time, cgi.escape(greeting.content)))
          self.response.out.write("""
</div>
    <hr align="center" width="100%" size="2" color="#c8c8c8" style="FILTER: alpha(opacity=100,finishopacity=0,style=3)">
    </td>
  </tr>
""")
      
      self.response.out.write("""
</table>
</div>
    """)

class login(webapp.RequestHandler):
  def get(self):
    self.response.out.write(
"""
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" type="text/css" media="screen" href="/css/style.css" />
<style type="text/css">
body {
font-family:'Helvetica Neue','Helvetica','Arial',sans-serif;
background-color: #404040;
}
</style>
<title>Miao Notes</title>

</head>
<body>
<div id="a1">Miao Notes</div>
<div class="aa1">
<form action="/main" method="post">
            <div id="a3"><input type="text" name="namea" /></div>
            <div id="a4"><input type="submit" value="<"></div>
</form>
</div>
</body>
</html>
""")


class MainPage(webapp.RequestHandler):
  def post(self):
    self.response.out.write(
"""
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" type="text/css" media="screen" href="/css/style.css" />
<title>Miao Notes</title>
</head>
<body>
""")

    def postb():
      global USERB
      global usertag
      USERB = self.request.get('namea')
      usertag = '#' + USERB
    postb()
    
    if USERB in USERA:
      self.response.out.write(
"""
<div id="b1">
<div id="b11">Miao~</div>
<div id="b12">Your notes it began</div>
<div id="b12">Add GTalk Friend<br>miaoapp2@appspot.com</div>
</div>
<div class="bb1">
<div id="b2">
""")
      self.response.out.write('Hello, ' + usertag + ', <a href="/"> Logout</a></div>')
      read(self)
      
    else:
      self.response.out.write('X')
      
    self.response.out.write("""</body></html>""")

#usertaga = usertag
class MainPagea(webapp.RequestHandler):
  def get(self):
    self.response.out.write(
"""
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" type="text/css" media="screen" href="/css/style.css" />
<title>Miao Notes</title>
</head>
<body>
<div id="b1">
<div id="b11">Miao~</div>
<div id="b12">Your notes it began</div>
<div id="b12">Add GTalk Friend<br>miaoapp2@appspot.com</div>
</div>
""")
    self.response.out.write(
"""
<div class="bb1">
<div id="b2">
""")
    self.response.out.write('Hello, ' + usertag + ', <a href="/"> Logout</a></div>')

    read(self)
      
    self.response.out.write("""</body></html>""")

class sign(webapp.RequestHandler):
  def post(self):
    greeting = Greeting()
    greeting.time = xmpp_handler.time
    greeting.author = usertag
    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/maina')

def main():
  application = webapp.WSGIApplication(
                                       [('/', login),
                                        ('/sign', sign),
                                        ('/maina', MainPagea),
                                        ('/main', MainPage)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
