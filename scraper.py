import scraperwiki

# Blank Python
import lxml.html
import lxml.etree
import ast
import re
import resource
import xlrd
import cookielib, urllib2, Cookie, urllib
import datetime, time
import random

from sys import exit

def getpoll():
    pageURL = "http://polldaddy.com/poll/7575405/"
    html = lxml.html.parse(pageURL).getroot()
    votebutton = html.cssselect('.vote-button')
    datavote = votebutton[0].get("data-vote")
    datadict = ast.literal_eval(datavote)
    return datadict    

def vote(data1):
    voteurl = "http://polldaddy.com/vote.php?va=" + data1['at'] + "&pt=" + data1['m'] + "&r=" + data1['b'] + "&p=" + repr(data1['id']) + "&a=" + urllib.quote_plus("34398490,") + "&o=&t=" + repr(data1['t']) + "&token=" + data1['n']
#    print(voteurl)
    result = lxml.html.parse(voteurl).getroot()

i = 0

token = ""

while i < 10000:
    j = 0
    while j == 0:
        data = getpoll()
        print data['n']
        if data['n'] <> token:
            j = 1
            token = data['n']
    vote(data)
    i += 1


