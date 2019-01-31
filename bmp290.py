#   Hafidh Satyanto
#   Reads Adafruit's BMP280 Library, and provides a defined function to be read off the master python file.

import board
import busio
import adafruit_bmp280      #Although we are using the BMP290, it is simply an upgraded version of the BMP280, and we are going to use the Adafruit Libraries.

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

bmp280.sea_level_pressure = 1032    # (mbar/hPa) Taken from NOAA data from Brookings Municipal Airport

def Get_Data():
    try:
        temperature = bmp280.temperature    #   In Celsius
        pressure = bmp280.pressure          #   In hPa
        altitude = bmp280.altitude          #   In Meters
        return temperature,pressure,altitude
    except IOError:
        print('BMP290 Connection Error')
        return 0,0,0

if __name__ == "__main__":
    Get_Data()

