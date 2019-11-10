
import csv
import time

MPL3115A2 = False
datarows = [
    'Time',
    'Pressure (kPa)',
    'Altitude (m)',
    'Altitude (ft)',
    'Temperature (C)',
]

while True:
    
    time.sleep(1)

    if (MPL3115A2 == True):
        MPL3115A2_Data - mpl3115a2.Get_Data()
    else:
        MPL3115A2_Data = [0, 0, 0]
        
try:
    import mpl3115a2
except Exception as E:
    print(E)
else:
    MPL3115A2 = True

filename = 'Data: '+time.strftime('%mm%dd%yy_%%Hh%Mm%Ss')+'.csv'

with open(filename, 'w') as csvfile:
    csvfile = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    
    #write first row
    csvfile.writerow(datarows)



with open(filename, 'a') as datafile:
    datalogger = csv.writer(datafile, delimiter=',', lineterminator='\n')
    datalogger.writerow([time.strftime('%m/%d/%Y %H:%M:%S%z'),
        str(MPL3115A2_Data[0]),                 # MPL3115A2 Pressure (kPa)
        str(MPL3115A2_Data[1]),                 # MPL3115A2 Temperature (kPa)
        str(MPL3115A2_Data[2]),                 # MPL3115A2 Altitude Estimation (m)
    ])