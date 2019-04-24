# Hafidh Satyanto
# When Raspberry Pi boots up, it will run this code.
# This code will import all the sensor codes as a Get_Data() function, and this code will
# write data to a CSV file line-by-line vertically using an array table. (So the array is
# inserted vertically per iteration as a CSV file).

import csv
import os
import time

LIS3DH = False
BMP280 = False
MPL3115A2 = False
GPS = False

deg = u'\N{DEGREE SIGN}'    # Degree Symbol
apo = u"\u0027"             # Apostrophe Symbol

# Search for BMP280 sensor connection
try: 
    import bmp280
except ImportError:
    print('Error importing BMP280 sensor')
    pass
else:
    BMP280 = True
    print('BMP280 sensor connected')

# Search for MPL3115A2 sensor connection
try:
    import mpl3115a2
except ImportError:
    print('Error importing MPL3115A2 sensor')
    pass
else:
    MPL3115A2 = True
    print('MPL3115A2 sensor connected')

# Search for LIS3DH sensor connection
try:
    import lis3dh
except ImportError:
    print('Error importing LIS3DH sensor')
    pass
else:
    LIS3DH = True
    print('LIS3DH sensor connected')

# Search for GPS sensor connection
try:
    import gps
except ImportError:
    print('Error importing GPS sensor')
    pass
else:
    GPS = True
    print('Adafruit GPS connected')


datarows = [
    'Time',                                                 #0
    'BMP280 Pressure (hPa)',                                #1
    'BMP280 Temperature (degrees C)',                       #2
    'BMP280 Altitude Estimation (m)',                       #3
    'MPL3115A2 Pressure (kPa)',                             #4
    'MPL3115A2 Temperature (degrees C)',                    #5
    'MPL3115A2 Altitude Estimation (m)',                    #6
    'LIS3DH Acceleration X (m/s^2)',                        #7
    'LIS3DH Acceleration Y (m/s^2)',                        #8
    'LIS3DH Acceleration Z (m/s^2)',                        #9
    'GPS Fix Timestamp (Hours)',                            #10
    'GPS Fix Timestamp (Minutes)',                          #11
    'GPS Fix Timestamp (Seconds)',                          #12
    'GPS Latitude (Degrees)',                               #13
    'GPS Longitude (Degrees)',                              #14
    'GPS # Satellites',                                     #15
    'GPS Altitude (meters)',                                #16
    'GPS Speed (knots)',                                    #17
    'GPS Track Angle (degrees)',                            #18
    'GPS Horizontal Dilution',                              #19
    'GPS Height Geo ID',                                    #20
]

if (BMP280==False):
    datarows[1] = 'BMP280 N/A',
    datarows[2] = 'BMP280 N/A',
    datarows[3] = 'BMP280 N/A',

if (MPL3115A2==False):
    datarows[4] = 'MPL3115A2 N/A',
    datarows[5] = 'MPL3115A2 N/A',
    datarows[6] = 'MPL3115A2 N/A',

if (LIS3DH==False):
    datarows[7] = 'LIS3DH N/A',
    datarows[8] = 'LIS3DH N/A',
    datarows[9] = 'LIS3DH N/A',

if (GPS==False):
    datarows[10] = 'GPS N/A',
    datarows[11] = 'GPS N/A',
    datarows[12] = 'GPS N/A',
    datarows[13] = 'GPS N/A',
    datarows[14] = 'GPS N/A',
    datarows[15] = 'GPS N/A',
    datarows[16] = 'GPS N/A',
    datarows[17] = 'GPS N/A',
    datarows[18] = 'GPS N/A',
    datarows[19] = 'GPS N/A',
    datarows[20] = 'GPS N/A',

csv_filename = 'Data: '+time.strftime('%mm%dd%yy_%Hh%Mm%Ss')+'.csv'
with open(csv_filename, 'w') as dataInit:
    dataInit = csv.writer(dataInit, delimiter=',', lineterminator='\n')
    dataInit.writerow(datarows)
        
while True:
    if (BMP280 == True):
        BMP280_Data = bmp280.Get_Data()
    else:
        BMP280_Data = [0, 0, 0]
    
    if (MPL3115A2 == True):
        MPL3115A2_Data = mpl3115a2.Get_Data()
    else:
        MPL3115A2_Data = [0, 0, 0]

    if (LIS3DH == True):
        LIS3DH_Data = lis3dh.Get_Data()
    else:
        LIS3DH_Data = [0, 0, 0]

    if (GPS == True):
        GPS_Data = gps.Get_Data()
    else:
        GPS_Data = [["Error","Error","Error"], "Error", "Error", "Error", "Error", "Error", "Error", "Error", "Error" ]
        # Time[Hours,Min,Secs],Latitude,Longitude,Satellites,Altitude,Speed,TrackAngle,HorizontalDilution,HeightGeoID


    # Datalog the sensor values and GPS data into a CSV file.
    with open(csv_filename, 'a') as csvFile:
        dataLogger = csv.writer(csvFile, delimiter=',', lineterminator='\n')
        dataLogger.writerow([time.strftime('%m/%d/%Y %H:%M:%S%z'),
            str(BMP280_Data[0]),                    # BMP280 Pressure (kPa)
            str(BMP280_Data[1]),                    # BMP280 Temperature (C)
            str(BMP280_Data[2]),                    # BMP280 Altitude Estimation (m)
            str(MPL3115A2_Data[0]),                 # MPL3115A2 Pressure (kPa)
            str(MPL3115A2_Data[1]),                 # MPL3115A2 Temperature (kPa)
            str(MPL3115A2_Data[2]),                 # MPL3115A2 Altitude Estimation (m)
            str(LIS3DH_Data[0]),                    # LIS3DH Acceleration X (m/s^2)
            str(LIS3DH_Data[1]),                    # LIS3DH Acceleration Y (m/s^2)
            str(LIS3DH_Data[2]),                    # LIS3DH Acceleration Z (m/s^2)
            GPS_Data[0][0],                         # GPS Fix Timestamp Hours
            GPS_Data[0][1],                         # GPS Fix Timestamp Minutes
            GPS_Data[0][2],                         # GPS Fix Timestamp Seconds
            GPS_Data[1],                            # GPS Latitude (Degrees)
            GPS_Data[2],                            # GPS Longitude (Degrees)
            GPS_Data[3],                            # GPS # Satellites
            GPS_Data[4],                            # GPS Altitude (meters)
            GPS_Data[5],                            # GPS Speed (knots)
            GPS_Data[6],                            # GPS Track Angle (degrees)
            GPS_Data[7],                            # GPS Horizontal Dilution
            GPS_Data[8],                            # GPS Height Geo ID
        ])


    # Form an APRS Packet using the Command Line
    aprs_Altitude = GPS_Data[4]
    aprs_Latitude = GPS_Data[1]
    aprs_Longitude = GPS_Data[2]
    aprs_Speed = GPS_Data[5]
    aprs_Pressure = BMP280_Data[0]
    aprs_Temperature = BMP280_Data[1]
    aprs_EAltitude = BMP280_Data[2]
    # Message = "HJ4 - Alt: {}, Lat: {:.6f}, Lon: {:.6f}, Spd: {}, Prs: {:02}, Tmp: {:01}, EAlt: {:01}".format(
    #     aprs_Altitude,aprs_Latitude,aprs_Longitude,aprs_Speed,aprs_Pressure,aprs_Temperature,aprs_EAltitude)
    Message = "HJ4 - Alt: "+GPS_Data[4]+", Lat: "+GPS_Data[1]+", Lon: "+GPS_Data[2]+", Spd: "+GPS_Data[5]+", Prs: {:2f}, Tmp: {:1f}, EAlt: {:1f}".format(BMP280_Data[0],BMP280_Data[1],BMP280_Data[2])
    WrappedMessage = '"{}"'.format(Message)
    APRScommand = "aprs -c KE0TSL -o aprspacket.wav " + WrappedMessage

    # Convert to .WAV file
    os.system(APRScommand)

    # Play .WAV file
    os.system("aplay aprspacket.wav")

    time.sleep(2.5) # Limited to GPS's timeout