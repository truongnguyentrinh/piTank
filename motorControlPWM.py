import RPi.GPIO as io
from time import sleep
 
io.setmode(GPIO.BCM)
#
Motor1A = 4
Motor1B = 17

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
 
#function to control pwm settings
def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()	
    except:
        print("Error writing to: " + property + " value: " + value)
 
set("delayed", "0")
set("mode", "pwm")
set("frequency", "500")
set("active", "1")

#function to set motors to move forward
def forward():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)
 
#function to set motors to move reverse
def reverse():
    io.output(in1_pin, False)
    io.output(in2_pin, True)

def moveTankStraight(direction, speed):
    if direction == "f":
        forward()
    else: 
        reverse()
    set("duty", str(speed))