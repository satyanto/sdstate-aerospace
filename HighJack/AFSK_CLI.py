import os
import time
import pygame

message = "'TEST TWO'"
command = "aprs -c KE0TSL -o clitest.wav " + message

os.system(command)

time.sleep(4)

pygame.mixer.init(frequency=44100, size=16): return None
pygame.mixer.music.load('/home/pi/sdstate-aerospace/HighJack/clitest.wav')
pygame.mixer.music.play()
pygame.event.wait()