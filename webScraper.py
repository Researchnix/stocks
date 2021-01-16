# web scpaper

from bs4 import BeautifulSoup
import requests
import simplejson as js


def url(ticker):
    return 'https://finance.yahoo.com/quote/' + ticker.upper()


def getData(ticker):
    f = requests.get(url(ticker))
    html = f.text
    try:
        i = html.index('summaryProfile')
        content = html[i:]
        a = content.index('{')
        b = content.index('}')
        raw = content[a:b+1]
    except ValueError:
        print('Stock not found')
    dic = js.loads(raw)
    return dic

def getIndustry(ticker):
    return getData(ticker)['industry']

def getSector(tkr):
    return getData(tkr)['sector']


