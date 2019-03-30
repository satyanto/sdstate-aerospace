import os
import time
from pydub import AudioSegment
from pydub.playback import play

message = "'TEST THREE WOOOOOHOOOO'"
command = "aprs -c KE0TSL -o testthree.wav " + message

os.system(command)

song = AudioSegment.from_wav("testthree.wav")
play(song)
