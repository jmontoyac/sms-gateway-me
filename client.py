import httplib, subprocess

c = httplib.HTTPConnection('http://159.65.168.11', 5002)
c.request('POST', '/', '{}')
doc = c.getresponse().read()
print doc