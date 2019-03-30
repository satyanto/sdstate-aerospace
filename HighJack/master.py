# Hafidh Satyanto
# When Raspberry Pi boots up, it will run this code.
# This code will import all the sensor codes as a Get_Data() function, and this code will
# write data to a CSV file line-by-line vertically using an array table. (So the array is
# inserted vertically per iteration as a CSV file).

import csv

BMP280 = False
MPL3115A2 = False

# Search for BMP280 sensor connection
try: 
    import bmp280.py
except ImportError:
    print('Error importing BMP280 sensor')
else:
    BMP280 = True
    print('BMP280 sensor connected')

# Search for MPL3115A2 sensor connection
try:
    import mpl3115a2.py
except ImportError:
    print('Error importing MPL3115A2 sensor')
else:
    MPL3115A2 = True
    print('MPL3115A2 sensor connected')

datarows = [
    'Time',                                         #0
    'Pressure',
    'Temperature',
]
    

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

    
    