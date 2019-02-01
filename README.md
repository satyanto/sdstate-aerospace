# sdstate-aerospace

![alt text](https://dl.boxcloud.com/api/2.0/internal_files/292366284127/versions/307734331615/representations/jpg_paged_2048x2048/content/1.jpg?access_token=1!hkpqK9opvPQ-nxyKLZchjsau7FiJKg90YJvIlU3ltqEf6VmYxveXwFwHdNgCrd9GTCdDHh3O3a7Qq3Mw1ST1hAPO8M-0uJoj5DtRvbTjhaWjA9pL12gUr428lCwTLUr092t-An8WwfsAAEu3G8an4vgPS7nd4wY0BVyE-4kox0dz3l_YPLvq2vuhH_GFu3cWekwTYv3hzLh_61Wo_jyeAWKTIUjmHMxh2UsLhXDnUXOGwpoonKmv8UZ0Bmgw4yULB4fzqAQz6g5lZSxh0N0U6Xs-l-hZk_QItlLxjE2NOUNH5HG8DDS90UBDH5J7acO-UUJqtBV7hCcp8GXusVOh0IA0-bHZrURdsKWrtHjVFUQSKqbIjUieyUFglYOU6t-ZPI8Rii0jGd15lJWP2LrfuENUOggvVueRvmkRpLQJ7IgzbHV-i9LWr_Ntw1y3CbMUk__ixY5fxBZ8C4CWEGx1_1LgDJBxB19y6ciJaJRx-WDqZrOs5orCOUPc6aCs7wDMLyG9Up0fDY6ihwXQAS35ORr3o_CBqp96U5aBu-OomUENkKwGRl0zl6dY0zkqGFeTGQ..&box_client_name=box-content-preview&box_client_version=1.61.0)

This is a compilation of all the code and hardware that is used for the cubesat/aerospace student organization at South Dakota State University.

Below you can see all the written documentation and how-to's regarding how to launch a high-altitude balloon or rocket and its related electrical components, and in this repository you can also view all necessary code and programming.


## New Raspberry Pi Set-Up
1. First, open up the terminal. We should first run standard updates for our Raspberry Pi:
```
sudo apt-get update
```
```
sudo apt-get upgrade
```
```
sudo pip3 install --upgrade setuptools
```
2. We will also enable the interface options I2C (for sensors - we'll be using the SDA/SCL ports), serial (for the GPS, which will use the UART's RX and TX ports.) We can enable these interfaces using the command below:
```
sudo raspi-config
```
3. Navigate to the interfaces options and then you can turn on the individual connections.
We also want to set up this github repository on our Raspberry Pi device, so we can download new code instantly and update it on-device if any changes are made to this online repository. We can do this by navigating into a folder and opening the terminal on that folder.
```
git clone https://github.com/Oreology/sdstate-aerospace
```
4. In order to update the local file on our Raspberry Pi device to the newest commits of this github repository, we can type:
```
git pull
```
This will mean that any changes to the code in this repository, will be 'pulled' into the local file on the Raspberry Pi.
This also enables us to type code in our laptops (a much better environment) rather than the Raspberry Pi, and have it automatically update on the Pi itself. This also allows us to store the code in an online environment, so if we lose a Raspberry Pi, we can always have the latest up-to-date codebase with all our programs ready to go.

5. Other necessities:
We would also want to enable the Raspberry Pi GPIO (General Purpose Input/Output) pins library, needed for Adafruit Blinka and we'll be using the Raspberry Pi's output pins to send either a HIGH or LOW signal:
```
pip3 install RPI.GPIO
```
Since we'll be using a lot of Adafruit-made sensors, we'll need to install their Adafruit Blinka library:
```
pip3 install adafruit-blinka
```


## Quick Command-Line References:
To check sensors that are connected through the I2C protocol:
```
sudo i2cdetect -y 1
```


## BMP280 Barometric Pressure, Temperature Sensor Set-Up
We are using the Adafruit BMP280, which uses a Bosch sensor to measure temperature and barometric pressure, and from both readings, we can estimate the altitude.
For this project, we are going to interface mainly with the I2C serial protocol.

|BMP280   |Raspberry Pi  |
|---------|--------------|
|VIN      | 3.3V         |
|GND      | GND          |
|SCK      | SCL          |
|SDI      | SDA          |

After connecting the wiring as above, we will use Adafruit's included BMP280 CircuitPython library. Since we already have installed Adafruit's Blinka library, all we have to do now is install this specific sensor's library, and we can do this by:
```
sudo pip3 install adafruit-circuitpython-bmp280
```

A python Get_Data() function for the BMP280 can be found in this repository. It uses the Adafruit's
BMP280 library but wraps it in another function for the sake of organization. Therefore, to use the BMP280 sensor, you can simply call the Get_Data() function after importing the bmp280.py python file.
An example can be found in the master python code (master.py)

## GPS Set-Up
We are using the Adafruit Ultimate GPS Breakout Board, but this should also work for most other GPS sensors.
First, connect the GPS to the Raspberry Pi accordingly:

|GPS      |Raspberry Pi  |
|---------|--------------|
|Vin      | 3.3V         |
|GND      | GND          |
|RX       | UART  TX     |
|TX       | UART  RX     |

Do note that, regarding this specific GPS sensor, it works better if you connect an external active antenna to the ANT port. It is not required, since it has a small lower-gain built-in ceramic antenna inside, but since we are going to be programming and developing inside a building, it is too weak to get a signal, hence we won't receive any data. I circumvented this by attaching an external antenna and then sticking the antenna on the window, which then allows me to obtain a connection.

1. First, we want to set up minicom, so we can test out the UART ports.
```
sudo apt-get install minicom
```
2. Edit the /boot/cmdline.txt file, so that it looks like this:
```
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait splash plymouth.ignore-serial-consoles
```
(single line)
What we are doing here is simply deleting references to ttyAMA0. To be honest, I don't quite understand it much myself.
3. To test out what sort of data we are receiving through the UART serial port, we can first change the settings for the minicom:
```
sudo minicom -s
```
Go to the serial port option, and change serial device to:     /dev/ttyS0
Go to Bps/Par/Bits, change baudrate to:     9600
4. We also want to install a NMEA parser, which will help us make the data that the GPS is sending to be more readable for us. Here is a link that also has some install instructions and how to set it up.
https://github.com/inmcm/micropyGPS

