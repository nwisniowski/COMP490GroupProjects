#!/usr/local/bin/python3

from lxml import html
from bs4 import BeautifulSoup
import requests

page = requests.get('https://stackoverflow.com/jobs/feed?location=bridgewater&range=50&distanceUnits=Miles')

tree = html.fromstring(page.content)

titles = tree.xpath('//title/text()')

descriptions = tree.xpath('//description/text()')

print ('Titles: '), titles