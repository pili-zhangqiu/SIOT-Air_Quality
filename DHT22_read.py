import Adafruit_DHT

def DHTread(pin):

  # Sensor should be set to Adafruit_DHT.DHT11,
  # Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
  sensor = Adafruit_DHT.DHT22
  
  # Try to grab a sensor reading.  Use the read_retry method which will retry up
  # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  
  if humidity is not None and temperature is not None:
    continue
  else:
    print('Failed to get reading. Try again!')
    
  return humidity, temperature;
