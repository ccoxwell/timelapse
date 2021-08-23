import picamera
import time

camera = picamera.PiCamera()
time.sleep(2)
camera.iso = 100
camera.awb_mode = 'sunlight'
camera.exposure_compensation = -1
camera.capture('test_image.jpg')
print('done')
