import urllib, urllib2
from flask import Flask, Response, session, request, url_for, redirect, render_template, abort, g, send_from_directory
from application import app
from application.functions import *

@app.route('/slack-invite/',methods=['GET','POST'])
def slackinvite():
    if request.method == 'POST':
        s = getSettings()
        email = request.form['email']
        url = 'https://'+s['slackSubdomain']+'.slack.com/api/users.admin.invite'
        values = {
          'token' : s['slackToken'],
          'email' : email,
          'set_active' : 'true',
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url,data)
        response = urllib2.urlopen(req)
        return redirect('/slack-invite/?success=1&email='+email)
    else:
        s = getSettings()
        return render_template('slackinvite/slackinvite.html',s=s)

