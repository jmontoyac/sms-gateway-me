# imports
import json
import urllib2
import config
 
# SMS Messages to send
data = {"https://smsgateway.me/api/v4/callback/66088211"}

req = urllib2.Request('https://smsgateway.me/api/v4/callback/17949')
req.add_header('Content-Type', 'application/json')
req.add_header('Authorization', config.authKey)

# Send request and get response
response = urllib2.urlopen(req)
json_data = json.load(response)

print ('Response: ' + str(json_data))
