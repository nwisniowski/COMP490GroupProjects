#!/usr/local/bin/python3

from lxml import html
from lxml import etree
import requests
import re
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

page = requests.get('https://stackoverflow.com/jobs/feed?location=bridgewater&range=50&distanceUnits=Miles')

etree = etree.fromstring(page.content)
tree = html.fromstring(page.content)

titles = tree.xpath('//title/text()')
links = etree.xpath('//item/link/text()')

userDefinedRange = input("How many jobs would you like to list? ")

while not userDefinedRange.isdigit():
	print ("Only integers are accepted!")
	userDefinedRange = input("Please input an integer: ")

userDefinedRange = int(userDefinedRange)

print ("\nFound " + str(len(titles) - 2) + " jobs on Stack Overflow. \n")

if len(titles) <= userDefinedRange:
	userDefinedRange = len(titles) - 2


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
