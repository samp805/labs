from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(4)
camera.capture('/home/pi/labs/labs/image1.jpg')
sleep(4)
camera.capture('/home/pi/labs/labs/image2.jpg')
sleep(4)
camera.capture('/home/pi/labs/labs/image3.jpg')
sleep(4)
camera.stop_preview()
