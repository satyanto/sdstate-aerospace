#   Hafidh Satyanto
#   Reads Adafruit's MPL3115A2 Library, and provides a defined function to be read off the master python file.

# import board
# import busio
# import adafruit_mpl3115a2

# i2c = busio.I2C(board.SCL, board.SDA)
# mpl3115a2 = adafruit_mpl3115a2.MPL3115A2(i2c)

# mpl3115a2.sealevel_pressure = 102030

# def Get_Data():
#     try: 
#         pressure = mpl3115a2.pressure           # In Pascals
#         altitude = mpl3115a2.altitude           # In Meters
#         temperature = mpl3115a2.temperature     # In Celsius

#         #testing purposes
#         print(pressure)
#         print(altitude)
#         print(temperature)

#         return pressure,altitude,temperature
#     except IOError:
#         print('MPL3115A2 Connection Error')
#         return 0,0,0

# if __name__ == "__main__":
#     Get_Data()


from smbus import SMBus
import time
bus = SMBus(1)

def Get_Data():
    try:
        bus.write_byte_data(0x60, 0x26, 0xB9)
        bus.write_byte_data(0x60, 0x13, 0x07)
        bus.write_byte_data(0x60, 0x26, 0xB9)
        #time.sleep(1)
        data = bus.read_i2c_block_data(0x60, 0x00, 6)
        altitude = (((data[1]*65536)+(data[2]*256)+(data[3]&0xF0))/16)/16
        temp = ((data[4]*256)+(data[5]&0xF0))/16
        ctemp = temp/16.0
        #ftemp = ctemp*1.8+32
        bus.write_byte_data(0x60, 0x26, 0x39)
        time.sleep(1)
        data=bus.read_i2c_block_data(0x60, 0x00, 4)
        press=((data[1]*65536)+(data[2]*256)+(data[3]&0xF0))/16.00
        pressure=(press/4.00)/1000.00 #given in kPa

        altitude = altitude - 23680

        return pressure,ctemp,altitude
    except IOError:
        print('MPL3115A2 Connection Error')
        return 0,0,0

if __name__ == "__main__":
    Get_Data()
