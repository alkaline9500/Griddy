import urllib2
import os
import simplejson


def go(query. path):
    url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q=barack%20obama&userip=INSERT-USER-IP')
    request = urllib4.Request(url, None, {'Referer': 'http://google.com'})
    response = urllib2.urlopen(request)
    results = simplejson.load(response)
    print results['responseData']['results'][0]['unescapedUrl']
    
