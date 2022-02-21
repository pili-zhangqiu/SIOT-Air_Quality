import time
import RPi.GPIO as GPIO
 
# Set the GPIO numbering scheme
GPIO.setmode(GPIO.BCM)
 
# Select the GPIO pins used for
# the encoder D0-D3 data inputs
GPIO.setup(17,GPIO.OUT,initial=0)
GPIO.setup(22,GPIO.OUT,initial=0)
GPIO.setup(23,GPIO.OUT,initial=0)
GPIO.setup(27,GPIO.OUT,initial=0)
 
# Select the GPIO pin to enable/disable the modulator
# Default to disabled
GPIO.setup(25, GPIO.OUT,initial=0)
 
# Select the signal used to select ASK/FSK
# Default to ASK
GPIO.setup(24, GPIO.OUT,initial=0)

# Socket 1 ON
D3=True
D2=True
D1=True
D0=True
 
# Set D0-D3
GPIO.output (27, D3)
GPIO.output (23, D2)
GPIO.output (22, D1)
GPIO.output (17, D0)
 
# Enable the modulator
def En_ON(){
   GPIO.output (25, True)
}

def En_OFF(){
   GPIO.output (25, False)
}
