# Reading each analog input from the ADS1x15
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# For web app
import RPi.GPIO as GPIO
MQpin=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from flask import Flask, render_template, request, send_file, make_response

app = Flask(__name__)


import sqlite3


#############################################################################
##         READ AND PLOT MQ135 values by reading from the ADS1115          ##
#############################################################################

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

# Main loop.
while True:
    # Read all the ADC channel values in a list.
    ADC_values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        ADC_values[i] = adc.read_adc(i, gain=GAIN)
        
        # Note you can also pass in an optional data_rate parameter that controls the ADC conversion time (in samples/second).
        # ADC_values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
               
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*ADC_values))
    # Pause for half a second.
    time.sleep(0.5)
    
