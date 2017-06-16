#!/bin/env python

import urllib2
import xml.etree.ElementTree as ET

response = urllib2.urlopen('http://www2.e-solat.gov.my/xml/today/?zon=SGR04')
html = response.read()

root = ET.fromstring(html)

for channel in root.iter('channel'):
    kawasan = channel.find('link').text

jadual=[]

for item in root.iter('item'):
    title=item[0].text
    desc=item[1].text
    waktu=[title,desc]
    jadual.append(waktu)

print "Waktu solat bagi kawasan %s" % kawasan
for solat, masa in jadual:
    print solat, masa
