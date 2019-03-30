import os
import time
import pygame

message = "'TEST TWO'"
command = "aprs -c KE0TSL -o clitest.wav " + message

os.system(command)

time.sleep(2)

pygame.mixer.init(frequency=44100, size=16)
pygame.mixer.music.load('/home/pi/sdstate-aerospace/HighJack/clitest.wav')
pygame.mixer.music.play()
