from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.start_preview()
time.sleep(10)
camera.capture('example.jpg')

camera.vflip = True

camera.capture('example2.jpg')

