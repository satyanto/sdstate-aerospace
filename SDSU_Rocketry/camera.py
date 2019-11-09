import picamera
from time import sleep
from subprocess import call

currentvideoticker = 0
readvideotickerfile = open("videoticker.txt","r")
currentvideoticker = int(readvideotickerfile.read())
readvideotickerfile.close()

writevideotickerfile = open("videoticker.txt","w")
writevideotickerfile.write(str(currentvideoticker+1))
writevideotickerfile.close()

with picamera.PiCamera() as camera: #setting up camera
        filename = "video"+str(currentvideoticker)
        camera.start_recording("/home/pi/Development/sdstate-aerospace/SDSU_Rocketry/"+filename+".h264") #start recording
        sleep(20) # time of video in seconds
        camera.stop_recording() #recording stopped
convert = "MP4Box -add /home/pi/Development/sdstate-aerospace/SDSU_Rocketry/+filename+".h264" /home/pi/Development/sdstate-aerospace/SDSU_Rocketry/"+filename+".mp4"
call([convert], shell=True) #executing convert using call
print("Video is Converted")