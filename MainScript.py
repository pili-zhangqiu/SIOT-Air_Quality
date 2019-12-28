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
    
#############################################################################
##                               Web App                                   ##
#############################################################################

'''
# Retrieve data from database

def getData():

        conn=sqlite3.connect('data/DHT.db')
        curs=conn.cursor()
        for row in curs.execute("SELECT * FROM DHT_DATA2 ORDER BY timestamp DESC LIMIT 1"):

                time = str(row[0])
                temp = row[1]
                hum = row[2]
                pulse = row[3]
                
        conn.close()

        return time, temp, hum, pulse

def getHistData (numSamples):
        conn=sqlite3.connect('data/DHT.db')
        conn=sqlite3.connect('data/DHT.db')
        curs=conn.cursor()
        curs.execute("SELECT * FROM DHT_data2 ORDER BY timestamp DESC LIMIT "+str(numSamples))
        data = curs.fetchall()
        dates = []
        temps = []
        hums = []
        pulse = []
        for row in reversed(data):
                dates.append(row[0])
                temps.append(row[1])
                hums.append(row[2])
                pulse.append(row[3])
        return dates, temps, hums, pulse
    
def maxRowsTable():
        conn=sqlite3.connect('data/DHT.db')
        curs=conn.cursor()
        for row in curs.execute("select COUNT(temp) from  DHT_data2"):
                maxNumberRows=row[0]
        return maxNumberRows
    
# define and initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
    numSamples = 100
# main route
@app.route("/")
def index():
        if(GPIO.input(MQpin)==1):
                warning="PPM detected, air contaminated"
        if(GPIO.input(MQpin)==0):
                warning="Air is clean, safe for breathing"
        chum,ctemp=Adafruit_DHT.read_retry(sensor,gpio)
        time, temp, hum ,pulse = getData()
        templateData = {
        'time'  : time,
        'temp'  : temp,
        'hum'   : hum,
        'pulse'   :pulse,
        'ctemp'   :ctemp,
        'chum'    :chum,
        'warning' :warning,
        'numSamples'   :numSamples
        }
        return render_template('index.html', **templateData)
@app.route('/', methods=['POST'])
def my_form_post():
    global numSamples
    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    time, temp, hum, pulse = getData()
    templateData = {
                'time'  : time,
                'temp'  : temp,
                'hum'   : hum,
                'pulse' : pulse,
                'numSamples'    : numSamples
        }
    return render_template('index.html', **templateData)
@app.route('/plot/temp')
def plot_temp():
        times, temps, hums, pulses = getHistData(numSamples)
        ys = temps
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Temperature [°C]")
        axis.set_xlabel("Samples")
        axis.grid(True)
        xs = range(numSamples)
        axis.plot(xs, ys)
        canvas = FigureCanvas(fig)
        output = io.BytesIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response
@app.route('/plot/hum')
def plot_hum():
        times, temps, hums, pulses = getHistData(numSamples)
        ys = temps
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Temperature [°C]")
        axis.set_xlabel("Samples")
        axis.grid(True)
        xs = range(numSamples)
        axis.plot(xs, ys)
        canvas = FigureCanvas(fig)
        output = io.BytesIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response
@app.route('/plot/hum')
def plot_hum():
        times, temps, hums, pulses = getHistData(numSamples)
        ys = hums
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Humidity [%]")
        axis.set_xlabel("Samples")
        axis.grid(True)
        xs = range(numSamples)
        axis.plot(xs, ys)
        canvas = FigureCanvas(fig)
        output = io.BytesIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response
@app.route('/plot/pulse')
def plot_pulse():
        times, temps, hums, pulses = getHistData(numSamples)
        ys = pulses
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Heart pulse [°C]")
        axis.set_xlabel("Samples")
        axis.grid(True)
        xs = range(numSamples)
        axis.plot(xs, ys)
        canvas = FigureCanvas(fig)
        output = io.BytesIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response

if __name__ == "__main__":

   app.run(host='0.0.0.0', port=80, debug=False)
   '''
