import os
import time

message = "'COMMAND LINE TEST WOOOOOHOOOO'"
command = "aprs -c KE0TSL -o cmdline.wav " + message

os.system(command)

os.system("aplay cmdline.wav")