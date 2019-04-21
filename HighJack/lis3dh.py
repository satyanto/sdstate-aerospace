import time
import board
import digitalio
import busio
import adafruit_lis3dh
i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

lis3dh.range = adafruit_lis3dh.RANGE_4_G

def Get_Data():
    try:
        x, y, z = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration]
        return x,y,z
    except IOError:
        print('LIS3DH Connection Error')
        return 0,0,0

if __name__ == "__main__":
    Get_Data()

