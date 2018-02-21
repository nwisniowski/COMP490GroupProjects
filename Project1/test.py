#!/usr/bin/env python
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

notify("Title", "Heres an alert")


print('http://www.example.com')

print ("Content-type: text/html")
print

print """
<html>
<head><title>Sample</title></head>
<body>
<a href='http://google.com'>google</a>
</body></html>
"""