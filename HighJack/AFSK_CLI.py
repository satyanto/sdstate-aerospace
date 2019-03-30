import os
import time
import pygame

pygame.init()

message = "'HELL YEAH BABY THIS CLI PROGRAM WORKS'"
command = "aprs -c KE0TSL -o clitest.wav " + message

os.system(command)

if os.path.isfile('/home/pi/sdstate-aerospace/HighJack/clitest.wav)'):
    #file exists
    aprs_wav = pygame.mixer.Sound('/home/pi/sdstate-aerospace/HighJack/clitest.wav')
    aprs_wav.play()
