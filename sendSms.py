# imports
import json
import urllib2
import config
from datetime import datetime
import time
import pprint

http_logger = urllib2.HTTPHandler(debuglevel = 1)
opener = urllib2.build_opener(http_logger)
urllib2.install_opener(opener)
 
# Formatear la fecha
timestamp = datetime.now()

# Cantidad de SMS a enviar
c = 2

# Send request and get response
def send_sms(sequence_number, fecha, phone_number):

  # Construir el SMS request
  req = urllib2.Request('https://smsgateway.me/api/v4/message/send')
  req.add_header('Content-Type', 'application/json')
  req.add_header('Authorization', config.authKey)

  # Contenido del SMS a enviar
  smsData = [
    {
      "phone_number": phone_number,
      "message": "SMS #" + str(sequence_number) + " sent on " + fecha,
      "device_id": config.celHuaweiId
    }
  ]
  response = urllib2.urlopen(req, json.dumps(smsData))
  json_data = json.load(response)
  print ('##### Response: ' + str(json_data))

# Enviar el SMS
for y in range(0, c):
  # Formatear la fecha
  timestamp = datetime.now()
  fecha_str = timestamp.strftime('%d %b %Y %H:%M:%S')
  send_sms(y+1, fecha_str, "8442283449")
  time.sleep(5)
