import os
import time
from pydub import AudioSegment
from pydub.playback import play

message = "'TEST TWO'"
command = "aprs -c KE0TSL -o testclis.wav " + message

os.system(command)

time.sleep(2)

song = AudioSegment.from_wav("testclis.wav")
play(song)
