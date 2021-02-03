import numpy as np
import cv2
import glob
from moviepy.editor import VideoFileClip
from mss import mss
from PIL import Image
import time

color = (0, 255, 0) # bounding box color.

# This defines the area on the screen.
mon = {'top' : 0, 'left' : 0, 'width' : 1920, 'height' : 1080}
sct = mss()
previous_time = 0
i = 0
lista = []
while i < 3000 :
    sct.get_pixels(mon)
    frame = Image.frombytes( 'RGB', (sct.width, sct.height), sct.image )
    frame = np.array(frame)
    lista.append(frame)
    # image = image[ ::2, ::2, : ] # can be used to downgrade the input
    txt1 = 'fps: %.1f' % ( 1./( time.time() - previous_time ))
    previous_time = time.time()
    print(txt1)
    i += 1
print(len(lista))