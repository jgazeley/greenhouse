import RPi.GPIO as io
import time
import datetime

io.setmode(io.BCM)
io.setwarnings(False)
io.setup(12, io.OUT)

while True:
    currTime = datetime.datetime.now()

    if (currTime.hour >= 7 and
        currTime.hour < 20 and
        io.input(12) != 0):

        io.output(12, 0)

    elif (currTime.hour >= 20 and
        io.input(12) != 1):

        io.output(12, 1)
