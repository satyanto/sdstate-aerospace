import os
import time

message = "'COMMAND LINE TEST WOOOOOHOOOO'"
command = "aprs -c KE0TSL -o cmdline.wav " + message

os.system(command)

os.system("aplay cmdline.wav")

i = 1
while i < 8:
    msg = "test: "
    loopmsg = '"{}"'.format(msg)
    loopcommand = "aprs -c KE0TSL -o cmdline.wav " + loopmsg
    os.system(loopcommand)
    os.system("aplay cmdline.wav")
    time.sleep(4)