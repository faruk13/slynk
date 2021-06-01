from flask import render_template, flash, redirect, url_for, session,request
from src import app #,db
from src.forms import enterURLForm
from src.models import enterURL
from src.services import *
import random
import string
#from validator_collection 
# import validators
import re


host = 'localhost:5000/'
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Slynk', sLinks=enterURL.query.all())


@app.route('/shorten', methods=['GET', 'POST'])
def shorten():
    form=enterURLForm()
    info=None
    if form.validate_on_submit():
        flash("URL entered url = {}".format(form.url.data))
        s = addShortUrl(form.url.data)
        if s is not None:
            flash(str(form.url.data+' URL shortened to '+ host + s), 'info')
            return redirect(url_for('index'))
        else:
            flash(str('Error'), 'info')
            return render_template('404.html',  info=info)
    
    return render_template('shorten.html', sLinks=enterURL.query.all(), form=form, info=info)


@app.route('/<string:short>')
def retURL(short):
    info=None    
    # o1=enterURL.query.filter_by(shortURL=str(short)).first()
    mappedUrl = getMappedUrl(short)
    if mappedUrl is not None:
        # longg=str(o1.longURL)
        return redirect(mappedUrl)
        # return mappedUrl
    else:
        flash(str('No URL has been shortened to ' + host + short), 'info')
        return render_template('404.html',  info=info)


@app.route('/about')
def about():  
    return render_template('about.html', title="About ")








