#!/usr/local/bin/python3

from lxml import html
from lxml import etree
import requests
import re
from textwrap import TextWrapper
import os
from sys import platform

def notify(title):
    os.system("""
              osascript -e 'display notification "{}" with title "New Job"'
              """.format(title))

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

userDefinedRange = input("How many jobs would you like to list? ")

while not userDefinedRange.isdigit():
	print ("FALSE")
	userDefinedRange = input("Please input an integer: ")

userDefinedRange = int(userDefinedRange)

for x in range(userDefinedRange):
	titleStr = str(titles[x+2])
	titleStr =  cleanhtml(titleStr)

	if platform == "darwin":
		notify(titleStr)
		print(titleStr)
		print (links[x])
		print ("\n")

	else:
		print(titleStr)
		print (links[x])
		print ("\n")



#    descStr = str(descriptions[x+1])
#    descStr =  cleanhtml(descStr)
#    descStr = cleanhtml2(descStr)
#    descStr = cleanhtml3(descStr)
#    print ("\n".join(tw.wrap(descStr)))
#    print("\n")




#print page.content
