#   Hafidh Satyanto
#   Reads Adafruit's MPL3115A2 Library, and provides a defined function to be read off the master python file.

import board
import busio
import adafruit_mpl3115a2

i2c = busio.I2C(board.SCL, board.SDA)
mpl3115a2 = adafruit_mpl3115a2.MPL3115A2(i2c)

mpl3115a2.sealevel_pressure = 102030

def Get_Data():
    try: 
        pressure = mpl3115a2.pressure           # In Pascals
        altitude = mpl3115a2.altitude           # In Meters
        temperature = mpl3115a2.temperature     # In Celsius

        #testing purposes
        print(pressure)
        print(altitude)
        print(temperature)

        return pressure,altitude,temperature
    except IOError:
        print('MPL3115A2 Connection Error')
        return 0,0,0

if __name__ == "__main__":
    Get_Data()