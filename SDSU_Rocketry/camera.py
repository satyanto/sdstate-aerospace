import picamera
from time import sleep
from subprocess import call

currentvideoticker = 0
videotickerfile = open("videoticker.txt","r+")
currentvideoticker = videotickerfile.read()
videotickerfile.write(currentvideoticker+1)
videotickerfile.close()


#with picamera.PiCamera() as camera: #setting up camera
#        camera.start_recording("/home/pi/Rocket_Software/video.h264") #start recording
#        sleep(20) # time of video in seconds
#        camera.stop_recording() #recording stopped
#convert = "MP4Box -add /home/pi/Rocket_Software/video.h264 /home/pi/Rocket_Software/new_video.mp4"
#call([convert], shell=True) #executing convert using call
#print("Video is Converted")