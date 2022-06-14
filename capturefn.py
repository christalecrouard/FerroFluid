import platform
from picamera import PiCamera
from time import sleep
import argparse
import sys


def capture(filename):
    
    path = filename

    camera = PiCamera()
    camera.resolution = (3280, 2464)
    camera.iso = 400
    camera.rotation=270
    sleep(5)
    camera.shutter_speed = 20000
    camera.capture(path)
    
    return path

