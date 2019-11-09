import picamera
from time import sleep
from subprocess import call

with picamera.PiCamera() as camera: #setting up camera
        camera.start_recording("/home/pi/Rocket_Software/video.h264") #start recording
        sleep(20) # time of video in seconds
        camera.stop_recording() #recording stopped
convert = "MP4Box -add /home/pi/Rocket_Software/video.h264 /home/pi/Rocket_Software/new_video.mp4"
call([convert], shell=True) #executing convert using call
pring("Video is Converted")