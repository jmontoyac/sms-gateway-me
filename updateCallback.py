# imports
import json
import urllib2
import config
 
# SMS Messages to send
data = {
  "name": "Test Callback Code",
  "event": "MESSAGE_RECEIVED",
  "device_id": config.celHuaweiId,
  "filter_type": "none",
  "filter": "",
  "method": "HTTP",
  "action": "http://159.65.168.11:5002",
  "secret": "super-secret"
}

req = urllib2.Request('https://smsgateway.me/api/v4/callback/17943')
req.add_header('Content-Type', 'application/json')
req.add_header('Authorization', config.authKey)

# Send request and get response
response = urllib2.urlopen(req, json.dumps(data))
json_data = json.load(response)

print ('Response: ' + str(json_data))
