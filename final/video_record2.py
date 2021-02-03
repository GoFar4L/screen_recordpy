import numpy as np
import pyautogui


class VideoRecord():
    def __init__(self, destArray):
        self.isRunning = False
        self.isPaused = False
        print('Video Recorder setted up')
    
    def record(self):
        try:
            print('Start Recording Video')   
            self.isRunning = True
            while self.isRunning:
                if self.isPaused:
                    print('Video Paused')
                    while self.isPaused:
                        print('Paused')
                    print('Video Resumed')
                img = pyautogui.screenshot()
                frame = np.array(img)
                destArray.append(frame)
            print('Video Record Ended')
            return destArray
        except:
            return False

    