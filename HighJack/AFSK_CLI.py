import os

message = "'HELL YEAH BABY THIS CLI PROGRAM WORKS'"
command = "aprs -c KE0TSL -o clitest.wav " + message

os.system(command)