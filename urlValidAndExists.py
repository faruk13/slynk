import re
from urllib.parse import urlparse
import httplib2
import urllib.parse as urlparse

regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def checkURLvalid(form,field):
    url=field.data
    if not re.match('(?:http|ftp|https)://', url):
        url="http://"+ url
        field.data=url   
    if not re.match(regex, url):
        raise ValidationError('Please enter a valid URL!')

def checkURLexists(form,field):
    try:
        p = urlparse.urlparse(field.data)
        conn = httplib2.HTTPConnectionWithTimeout(p.netloc)
        conn.request('HEAD', p.path)
        resp = conn.getresponse()
    except:
        raise ValidationError("URL doesn't resolve. Are you sure it's correct?")

