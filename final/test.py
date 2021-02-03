from multiprocessing import Pool, TimeoutError
import time
import os
from audio_record import AudioRecord
from video_record import VideoRecord
from keyboard_input import KeyBoardInput

if __name__ == '__main__':
    v = VideoRecord('output.mp4')
    a = AudioRecord('output.wav')
    k = KeyBoardInput()

    with Pool(processes=2) as pool:
       
        video = pool.apply_async(v.record)
        audio = pool.apply_async(a.record)
        videores = video.get(None)
        audiores = audio.get(None)
        
        print(videores)             
        print(audiores)
    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")