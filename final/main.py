import threading
from multiprocessing import Process
from video_record2 import VideoRecord
from audio_record import AudioRecord
from keyboard_input import KeyBoardInput
from time import sleep

if __name__=="__main__":
    output = "Video"
    a = AudioRecord(output)
    v = VideoRecord(output)
    kb = KeyBoardInput()





