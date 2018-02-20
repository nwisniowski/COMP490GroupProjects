#!/usr/local/bin/python3

from lxml import html
from lxml import etree
import requests
import re
from textwrap import TextWrapper


#remove html tags
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, ' ', raw_html)
  return cleantext

#remove paragraph/font tags
def cleanhtml2(raw_html):
  cleanr = re.compile('&.*?;')
  cleantext = re.sub(cleanr, ' ', raw_html)
  return cleantext

#remove extra spaces
def cleanhtml3(raw_html):
  cleanr = re.compile(' +')
  cleantext = re.sub(cleanr, ' ', raw_html)
  return cleantext

tw = TextWrapper()
tw.width = 80

page = requests.get('https://stackoverflow.com/jobs/feed?location=bridgewater&range=50&distanceUnits=Miles')

etree = etree.fromstring(page.content)
tree = html.fromstring(page.content)

titles = tree.xpath('//title/text()')

descriptions = tree.xpath('//description/text()')

links = etree.xpath('//item/link/text()')

for x in range(20):
    titleStr = str(titles[x+2])
    titleStr =  cleanhtml(titleStr)
    print("Title: " + titleStr)
    print ("Link: " + links[x])
    print ("\n")


#    descStr = str(descriptions[x+1])
#    descStr =  cleanhtml(descStr)
#    descStr = cleanhtml2(descStr)
#    descStr = cleanhtml3(descStr)
#    print ("\n".join(tw.wrap(descStr)))
#    print("\n")




#print page.content
