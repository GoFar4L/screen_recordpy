import keyboard

class KeyBoardInput():
    def __init__(self, audioRecord, videoRecord):
        self.AudioR = audioRecord
        self.VideoR = videoRecord
        self.isRunning = False
        self.isPaused = False

    def start(self):
        self.isRunning = True
        while self.isRunning:
            if keyboard.is_pressed('s'):
                if keyboard.is_pressed('t'):
                    self.VideoR.isRunning = False
                    self.AudioR.isRunning = False
                    self.isRunning = False
                    print('Stopped')
            if keyboard.is_pressed('p'):
                if keyboard.is_pressed('a'):
                    self.VideoR.isPaused = True
                    self.AudioR.isPaused = True
                    self.isPaused = True
                    print('Paused')
                    while self.isPaused:
                        if keyboard.is_pressed('p'):
                            if keyboard.is_pressed('a'):
                                print('Resumed')
                                self.VideoR.isPaused = False
                                self.AudioR.isPaused = False
                                self.isPaused = False

                    
        
