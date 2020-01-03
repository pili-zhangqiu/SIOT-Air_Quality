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

# Import the library calculating PPM values for the MQ135
from MQ135_Calibrate import MQ135_Values

def main():  
  
    #while True:
        
        # Read air quality values from the MQ135 sensors
        ADC_values = ADCread()

        ADC0 = ADC_values[0]    # Air Quality Inside
        ADC1 = ADC_values[1] -2550    # Air Quality Outside
        
        # Read temperature and humidity values from the DHT22 sensors
        DHT_pin0 = 23
        DHT_pin1 = 24

        DHT_h0, DHT_t0 = DHTread(DHT_pin0)
        DHT_h1, DHT_t1 = DHTread(DHT_pin1)
        
        # Calculate PPM ---------------------------------------------
        RZ0, c_RZ0, PPM0, c_PPM0 = MQ135_Values(ADC0,DHT_t0,DHT_h0)
        RZ1, c_RZ1, PPM1, c_PPM1 = MQ135_Values(ADC1,DHT_t1,DHT_h1)

        # Print values on the command prompt
        print('Values Inside')
        print('Air Quality: Concentration of CO is %f PPM' % PPM0)  
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(DHT_t0, DHT_h0))  
        print(' ')
        print('Values Outside')
        print('Air Quality: Concentration of CO is %f PPM' % PPM1)  
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(DHT_t1, DHT_h1)) 
        print ('-' *30)

        update_sheet("Sheet1", ADC0, PPM0, ADC1, PPM1, DHT_t0, DHT_h0, DHT_t1, DHT_h1)
       # time.sleep(60)

if __name__ == '__main__':  
    main()
