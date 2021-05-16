from flask import render_template, flash, redirect,  url_for, session,request
from App import app,db
from App.forms import enterURLForm
from App.models import enterURL
import random
import string
#from validator_collection 
import validators
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
        
        flash("URL entered url = {}".format(form.url.data ))
        extra="!"+"@"+"*" #using hash# makes to take no more chars in the link
        chars = string.ascii_letters + string.digits + extra
    
        def randString():
            return "".join(random.choice(chars) for x in range(5))
                        #''.join(random.choices(chars, k=N)) same but simplified
                       #''.join(random.SystemRandom().choice(chars) for i in range(N)) more secure  
        s= random.choice(string.ascii_letters) + randString()
                        #so that "extra" chars don't start the s

        u=enterURL(longURL=form.url.data, shortURL=s)
        
        db.session.add(u)
        db.session.commit()
        flash(str(form.url.data+' URL shortened to '+ host + s), 'info')
        return redirect(url_for('index'))
    
    return render_template('shorten.html', sLinks=enterURL.query.all(), form=form, info=info)

@app.route('/<string:short>')
def retURL(short):
    info=None    
    o1=enterURL.query.filter_by(shortURL=str(short)).first()
    if o1 is not None:
        longg=str(o1.longURL)
        return redirect(longg)
    else:
        flash(str('No URL has been shortened to ' + host + short), 'info')
        return render_template('404.html',  info=info)

@app.route('/about')
def about():  
    return render_template('about.html', title="About ")








