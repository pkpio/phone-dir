#!/usr/bin/env python

# Developer:	Praveen Kumar Pendyala
# Created:	24/05/2014
# 
# This is just an attempt to make a full fledged crawler to make a database of phone numbers. All of them! Yeah baby.

import urllib
import time

start = time.time()


reponse = urllib.urlopen('http://callerpy.sysbase.org/search/world/api/v1/REST?number=920012345&cc=966');
print reponse.read()
reponse = urllib.urlopen('http://callerpy.sysbase.org/search/world/api/v1/REST?number=8828829765&cc=91');
print reponse.read()
reponse = urllib.urlopen('http://callerpy.sysbase.org/search/world/api/v1/REST?number=8828829765&cc=91');
print reponse.read()
reponse = urllib.urlopen('http://callerpy.sysbase.org/search/world/api/v1/REST?number=8828829765&cc=91');
print reponse.read()


time = time.time() - start 

print 'took: ' + repr(time)
