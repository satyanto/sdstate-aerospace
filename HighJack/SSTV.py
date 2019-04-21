import os
import time

pic = "raspistill -t 1 --width 320 --height 256 -e png -o /tmp/image.png "
text1 = "sudo convert /tmp/image.png -pointsize 36 -fill black -annotate +01+30 "
callsign = "KEOSTL"
text2 = '"{}"'.format(callsign)
text3 = " /tmp/image.png"
text = text1+text2+text3 
convert = " /home/pi/sstv/pisstv/pisstv /tmp/image.png 22050"
play = "aplay /tmp/image.png.wav"
move = "mv /tmp/image.png /home/pi/Pictures"

i = 1

while True:
	rename = "mv /home/pi/Pictures/image.png  /home/pi/Pictures/image{}.png" .format(str(i))
	os.system(pic)
	os.system(text)
	time.sleep(1)
	os.system(convert)
	os.system(play)
	os.system(move)
	os.system(rename)
	time.sleep(5*60)