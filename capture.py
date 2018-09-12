from picamera import PiCamera
from time import sleep

camera = PiCamera()

filename = input('Input the filename:  ')
camera.start_preview()
sleep(15)
camera.capture('/home/pi/labs/labs/' + filename)
camera.stop_preview()
