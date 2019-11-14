
import csv
import os
import time
import subprocess
import os
import picamera
from time import sleep
from subprocess import call

t=30     #time in seconds

x=os.fork()
if x:
    #import camera_test
    timeout = time.time() + t   # t sec from now

    while True:
        currentvideoticker = 0
        readvideotickerfile = open("videoticker.txt","r")
        currentvideoticker = int(readvideotickerfile.read())
        readvideotickerfile.close()

        writevideotickerfile = open("videoticker.txt","w")
        writevideotickerfile.write(str(currentvideoticker+1))
        writevideotickerfile.close()

        with picamera.PiCamera() as camera: #setting up camera
                filename = "video"+str(currentvideoticker)
                camera.start_recording("/home/pi/Development/sdstate-aerospace/SDSU_Rocketry/videos.h264/"+filename+".h264") #start recording
                time.sleep(t)
                camera.stop_recording() #recording stopped
        convert = "MP4Box -add /home/pi/Development/sdstate-aerospace/SDSU_Rocketry/videos.h264/"+filename+".h264 /home/pi/Development/sdstate-aerospace/SDSU_Rocketry/videos.mp4/"+filename+".mp4"
        call([convert], shell=True) #executing convert using call
        print("Video is Converted") 
        break
        
        


else:




    MPL3115A2 = False

    deg = u'\N{DEGREE SIGN}'    # Degree Symbol
    apo = u"\u0027"             # Apostrophe Symbol


    # Search for MPL3115A2 sensor connection
    try:
        import mpl3115a2
    except Exception as E:
        print('Error importing MPL3115A2 sensor')
        print(E)
    else:
        MPL3115A2 = True
        print('MPL3115A2 sensor connected')

    datarows = [
        'Time',                                                 #0
        'MPL3115A2 Pressure (kPa)',                             #1
        'MPL3115A2 Temperature (degrees C)',                    #2
        'MPL3115A2 Altitude (m)',                               #3
    ] 

    if (MPL3115A2==False):
        datarows[4] = 'MPL3115A2 N/A',
        datarows[5] = 'MPL3115A2 N/A',
        datarows[6] = 'MPL3115A2 N/A',

    csv_filename = 'Data: '+time.strftime('%mm%dd%yy_%Hh%Mm%Ss')+'.csv'
    with open(csv_filename, 'w') as dataInit:
        dataInit = csv.writer(dataInit, delimiter=',', lineterminator='\n')
        dataInit.writerow(datarows)

    timeout = time.time() + t   # t sec from now
        
    while True:
    
        if (MPL3115A2 == True):
            MPL3115A2_Data = mpl3115a2.Get_Data()
        else:
            MPL3115A2_Data = [0, 0, 0]

        # Datalog the sensor values and GPS data into a CSV file.
        with open(csv_filename, 'a') as csvFile:
            dataLogger = csv.writer(csvFile, delimiter=',', lineterminator='\n')
            dataLogger.writerow([time.strftime('%m/%d/%Y %H:%M:%S%z'),
                str(MPL3115A2_Data[0]),                 # MPL3115A2 Pressure (kPa)
                str(MPL3115A2_Data[1]),                 # MPL3115A2 Temperature (K)
                str(MPL3115A2_Data[2]),                 # MPL3115A2 Altitude Estimation (m)
        ])

        if time.time() > timeout:
            break
  
