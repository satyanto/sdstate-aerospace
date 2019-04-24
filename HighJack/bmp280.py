#   Hafidh Satyanto
#   Reads Adafruit's BMP280 Library, and provides a defined function to be read off the master python file.

import board
import busio
import adafruit_bmp280      # We are going to use Adafruit's library as a driver for this sensor.

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

bmp280.sea_level_pressure = 1016    # (mbar/hPa) Taken from NOAA data from Brookings Municipal Airport

def Get_Data():
    try:
        temperature = bmp280.temperature    #   In Celsius
        pressure = bmp280.pressure          #   In hPa / mbar
        altitude = bmp280.altitude          #   In Meters

        #testing purposes
        print(temperature)
        print(pressure)
        print(altitude)

        return pressure,temperature,altitude
    except Exception as E:
        print('BMP280 Connection Error')
        print(E)
        return 0,0,0

if __name__ == "__main__":
    Get_Data()
