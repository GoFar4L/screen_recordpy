import cv2 as cv
import numpy as np
import pyautogui
import sys
import keyboard
import time


def exit():
    if keyboard.is_pressed('s'):
        if keyboard.is_pressed('t'):
            print('Exiting')
            return True
    else:
        return False
        
def pause():
    if keyboard.is_pressed('p'):
        if keyboard.is_pressed('o'):
            print('Paused')
            return True
    else:
        return False

def stop_pause():
    if keyboard.is_pressed('p'):
        if keyboard.is_pressed('a'):
            print('Resume')
            return True
    else:
        return False


fps = 30.0

screensize = (1920, 1080)
four_char_code = cv.VideoWriter_fourcc(*"mp4v")
writer = cv.VideoWriter("record.mp4", four_char_code, fps, (screensize))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    writer.write(rgb_frame)
    if exit():
        writer.release()
        sys.exit()
    if pause():
        flag = True
        while flag:
            if(stop_pause()):
                flag = False
    