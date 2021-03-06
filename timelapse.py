from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
	camera.iso = 100
	camera.awb_mode = 'sunlight'
	camera.exposure_compensation = 0
	sleep(2)
	for filename in camera.capture_continuous('img{counter:04d}.jpg'):
		print('Captured %s' % filename)
		sleep(15)
