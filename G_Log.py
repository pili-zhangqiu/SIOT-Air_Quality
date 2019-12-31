# Import libraries
from __future__ import print_function  
import datetime
import time

# Import the function to update Google Sheet
from G_UpdateSheet import update_sheet

# Import the function reading the ADC values from both MQ135 sensors (Air Quality)
from ADS1x15_read import ADCread

# Import the library reading the DHT22 values (Temperature and Humidity)
from DHT22_read import DHTread

def main():  
  
    #while True:
        
        # Read air quality values from the MQ135 sensors
        ADC_values = ADCread()

        ADC0 = ADC_values[0]    # Air Quality Inside
        ADC1 = ADC_values[1] -2544    # Air Quality Outside
        
        # Calculate PPM
        RL = 10
        PPM0 = (RL * (6204.5 - ADC0)) / ADC0;
        PPM1 = (RL * (6204.5 - ADC1)) / ADC1;     
        
        # Read temperature and humidity values from the DHT22 sensors
        DHT_pin0 = 23
        DHT_pin1 = 24

        DHT_h0, DHT_t0 = DHTread(DHT_pin0)
        DHT_h1, DHT_t1 = DHTread(DHT_pin1)


        # Print values on the command prompt
        print('Air Quality in PPM')
        print('Inside={0:0.1f}  Outside={1:0.1f}'.format(PPM0, PPM1)) 
        print(' ')
        print('Values Inside')
        print ('Air Quality: %f PPM' % ADC0)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(DHT_t0, DHT_h0))  
        print(' ')
        print('Values Outside')
        print ('Air Quality: %f PPM' % ADC1)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(DHT_t1, DHT_h1)) 
        print ('-' *30)

        update_sheet("Sheet1", ADC0, ADC1, DHT_t0, DHT_h0, DHT_t1, DHT_h1)
       # time.sleep(60)

if __name__ == '__main__':  
    main()
