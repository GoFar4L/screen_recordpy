import cv2 as cv
import numpy as np
import pyautogui


class VideoRecord():
    def __init__(self, outputName):
        self.FPS = 30.0
        self.OUTPUT_FILENAME = outputName
        self.SCREENSIZE = (1920,1080)
        self.FOUR_CHAR_CODE = cv.VideoWriter_fourcc(*"mp4v")
        self.isRunning = False
        self.isPaused = False
        print('Video Recorder setted up')
    
    def record(self):
        try:
            print('Start Recording Video')
            writer = cv.VideoWriter(self.OUTPUT_FILENAME, self.FOUR_CHAR_CODE, self.FPS, (self.SCREENSIZE)) 
            self.isRunning = True
            while self.isRunning:
                if self.isPaused:
                    print('Video Paused')
                    while self.isPaused:
                        print('Paused')
                    print('Video Resumed')
                img = pyautogui.screenshot()
                frame = np.array(img)
                rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                writer.write(rgb_frame)
            writer.release()
            print('Video Record Ended')
            return True
        except:
            return False

    