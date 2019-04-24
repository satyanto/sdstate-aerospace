
import time
import board
import busio

import adafruit_gps

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

gps = adafruit_gps.GPS(uart, debug=False)

gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b'PMTK220,1000')

def Get_Data():
    try:
        gps.update()
        if gps.has_fix:
            Time = [
                "{:02}".format(gps.timestamp_utc.tm_hour),
                "{:02}".format(gps.timestamp_utc.tm_min),
                "{:02}".format(gps.timestamp_utc.tm_sec),
            ]
            Latitude = "{0:.6f}".format(gps.latitude)     # degrees
            Longitude = "{0:.6f}".format(gps.longitude)   # degrees
            if gps.satellites is not None:
                Satellites = "{}".format(gps.satellites)
            else:
                Satellites = "None"
            if gps.altitude_m is not None:
                Altitude = "{}".format(gps.altitude_m)
            else:
                Altitude = "None"
            if gps.speed_knots is not None:
                Speed = "{}".format(gps.speed_knots)
            else:
                Speed = "None"
            if gps.track_angle_deg is not None:
                TrackAngle = "{}".format(gps.track_angle_deg)
            else:
                TrackAngle = "None"
            if gps.horizontal_dilution is not None:
                HorizontalDilution = "{}".format(gps.horizontal_dilution)
            else:
                HorizontalDilution = "None"
            if gps.height_geoid is not None:
                HeightGeoID = "{}".format(gps.height_geoid)
            else:
                HeightGeoID = "None"

            return Time,Latitude,Longitude,Satellites,Altitude,Speed,TrackAngle,HorizontalDilution,HeightGeoID
        elif not gps.has_fix:
            Time = [
                "No Fix",
                "No Fix",
                "No Fix",
            ]
            Latitude = "No Fix"
            Longitude = "No Fix"
            Satellites = "No Fix"
            Altitude = "No Fix"
            Speed = "No Fix"
            TrackAngle = "No Fix"
            HorizontalDilution = "No Fix"
            HeightGeoID = "No Fix"

            return Time,Latitude,Longitude,Satellites,Altitude,Speed,TrackAngle,HorizontalDilution,HeightGeoID
    except Exception as E:
        print("GPS Connection Error")
        print(E)
        Time = [
            "Error",
            "Error",
            "Error",
        ]
        Latitude = "Error"
        Longitude = "Error"
        Satellites = "Error"
        Altitude = "Error"
        Speed = "Error"
        TrackAngle = "Error"
        HorizontalDilution = "Error"
        HeightGeoID = "Error"

        return Time,Latitude,Longitude,Satellites,Altitude,Speed,TrackAngle,HorizontalDilution,HeightGeoID



if __name__ == "__main__":
    Get_Data()
