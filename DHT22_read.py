import Adafruit_DHT

def DHTread(sensor,pin)
  # Try to grab a sensor reading.  Use the read_retry method which will retry up
  # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
  humidity, temperature = Adafruit_DHT.read_retry(sensorDHT, pin)
  
  if humidity is not None and temperature is not None:
    continue
  else:
    print('Failed to get reading. Try again!')
