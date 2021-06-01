from src import app, db
import random, string
from src.models import enterURL

def randString():
    extra="!"+"@"+"*" #using hash# makes to take no more chars in the link
    chars = string.ascii_letters + string.digits + extra
    return "".join(random.choice(chars) for x in range(5))
                #''.join(random.choices(chars, k=N)) same but simplified
                #''.join(random.SystemRandom().choice(chars) for i in range(N)) more secure 

def generateShortUrl():
    s = random.choice(string.ascii_letters) + randString()
    #so that "extra" chars don't start the s
    return s

def getMappedUrl(sUrl):
    lUrl=enterURL.query.filter_by(shortURL=str(sUrl)).first()
    if lUrl is not None:
        return lUrl.longURL
    return None

def addShortUrl(lUrl):
    sUrl = generateShortUrl()
    try:
        u = enterURL(longURL=lUrl, shortURL=sUrl)
        db.session.add(u)
        db.session.commit()
        status = 201
    except:
        db.session.rollback()
        status = 400
    return sUrl if status == 201 else None



    
    