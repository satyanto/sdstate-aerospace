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

# i2c_address = 0x60
# ctrl_reg1 = 0x26
# pt_data_cfg = 0x13
bus = SMBus(1)

# setting = bus.read_byte_data(i2c_address, ctrl_reg1)
# newsetting = setting | 0x38
# bus.write_byte_data(i2c_address, ctrl_reg1, newsetting)

# bus.write_byte_data(i2c_address, pt_data_cfg, 0x07)

# setting = bus.read_byte_data(i2c_address, ctrl_reg1)
# if (setting & 0x02) == 0:
#     bus.write_byte_data(i2c_address, ctrl_reg1, (setting | 0x02))

def Get_Data():
    try:
        # pressure_data = bus.read_i2c_block_data(i2c_address,0x01,3)
        # temperature_data = bus.read_i2c_block_data(i2c_address,0x04,2)
        
        # p_msb = pressure_data[0]
        # p_csb = pressure_data[1]
        # p_lsb = pressure_data[2]
        # t_msb = temperature_data[0]
        # t_lsb = temperature_data[1]

        # pressure = (p_msb << 10) | (p_csb << 2) | (p_lsb >> 6)
        # p_decimal = ((p_lsb & 0x30) >> 4)/4.0

        # celsius = t_msb + (t_lsb >> 4)/16.0
        






        bus.write_byte_data(0x60, 0x26, 0xB9)
        bus.write_byte_data(0x60, 0x13, 0x07)
        bus.write_byte_data(0x60, 0x26, 0xB9)
        time.sleep(1)

        data = bus.read_i2c_block_data(0x60, 0x00, 6)
        theight = ((data[1]*65536)+(data[2]*256)+(data[3] & 0xF0))/16
        temp = ((data[4]*256)+(data[5] & 0xF0))/16
        altitude = theight/16
        ctemp = temp/16

        bus.write_byte_data(0x60, 0x26, 0x39)
        time.sleep(1)
        data=bus.read_i2c_block_data(0x60, 0x00, 4)
        press=((data[1]*65536)+(data[2]*256)+(data[3] & 0xF0))/16
        pressure=(press/4.00)/1000.00 #given in kPa

        #altitude = altitude - 23680

        return pressure,ctemp,altitude
    except Exception as E:
        print('MPL3115A2 Connection Error')
        print(E)
        return 0,0,0

if __name__ == "__main__":
    Get_Data()
