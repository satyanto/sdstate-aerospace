import os
import time
import pygame

message = "'TEST TWO'"
command = "aprs -c KE0TSL -o clitest.wav " + message

os.system(command)

time.sleep(4)

pygame.mixer.init()
aprs_wav = pygame.mixer.load('/home/pi/sdstate-aerospace/HighJack/clitest.wav')
aprs_wav.play()
