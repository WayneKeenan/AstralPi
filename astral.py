#!/usr/bin/env python3

from time import sleep
import pantilthat
from vrzero.hmd import OpenHMD
import atexit

@atexit.register
def close():
        print("Shutting servos down")
        pantilthat.servo_enable(1, False)
        pantilthat.servo_enable(2, False)



hmd = OpenHMD()

PAN_OFFSET = -35     # -ve is up
TILT_OFFSET = -30    # -ve is right

while True:
        hmd.poll()
        x_rot = float(hmd.rotation[0])
        y_rot = float(hmd.rotation[1])
        z_rot = float(hmd.rotation[2])

        tilt = int( y_rot * 90 ) + TILT_OFFSET
        pan  = int( x_rot * -90 ) + PAN_OFFSET

        tilt = max(-90, min(tilt, 90))
        pan = max(-90, min(pan, 90))

        print("HMD({:+.2f}, {:+.2f}, {:+.2f}) => PanTilt({}, {})".format(x_rot, y_rot, z_rot, pan, tilt))
        pantilthat.tilt(tilt)
        pantilthat.pan(pan)

        sleep(0.01)

