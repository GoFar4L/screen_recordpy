import pyautogui
import cv2 as cv
import numpy as np
import keyboard

def pause():
    if keyboard.is_pressed('p'):
        if keyboard.is_pressed('2'):
            print('Video Paused')
            return True
    else:
        return False

def exit():
    if keyboard.is_pressed('s'):
        if keyboard.is_pressed('2'):
            print('Video Ended')
            return True
    else:
        return False



flag = False
img_list = []
is_running = True


while is_running:
    img = pyautogui.screenshot()
    img_list.append(img)

    if exit():
        is_running = False

    if pause():
        flag = True
        while flag:
            if(pause()):
                flag = False


fps = 30.0
screensize = (1920, 1080)
four_char_code = cv.VideoWriter_fourcc(*"mp4v")
writer = cv.VideoWriter("record.mp4", four_char_code, fps, (screensize))

for img in img_list:
    frame = np.array(img)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    writer.write(rgb_frame)

writer.release()