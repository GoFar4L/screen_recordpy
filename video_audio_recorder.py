import cv2 as cv
import numpy as np
import pyautogui
import sys
import keyboard
import time
import pyaudio
import wave
import threading
import ffmpeg


#Global variables
stop_ = False
pause_ = False
A_OUTPUT_FILENAME = "audio_record.wav"

#Exit and Pause Function
def exit():
    global stop_
    while not stop_:
        if keyboard.is_pressed('s'):
            if keyboard.is_pressed('t'):
                print('Exiting')
                stop_ = True
                

thread1 = threading.Thread(target=exit, daemon=True, name="stop").start()

def pause():
    global pause_
    while not pause_:
        if keyboard.is_pressed('p'):
            if keyboard.is_pressed('o'):
                print('Paused')
                pause_ = not pause
            

thread2 = threading.Thread(target=pause, daemon=True, name="pause").start()

def record_audio():
    #Audio settings
    global stop_
    global pause_
    global A_OUTPUT_FILENAME

    A_FORMAT = pyaudio.paInt16
    A_CHANNELS = 2
    A_RATE = 44100
    A_CHUNK = 1024
    #Starting audio
    frames = []
    audio = pyaudio.PyAudio()
    stream = audio.open(format=A_FORMAT, channels=A_CHANNELS,
                        rate=A_RATE, input=True,
                        frames_per_buffer=A_CHUNK)
    while not stop_:
        #Store Audio
        data = stream.read(A_CHUNK)
        frames.append(data)
        #Pause Logic
        if pause_:
            while pause_:
                pass

    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile = wave.open(A_OUTPUT_FILENAME, 'wb')
    print('closing audio')
    waveFile.setnchannels(A_CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(A_FORMAT))
    waveFile.setframerate(A_RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()





#Video settings
FPS = 30.0
SCREENSIZE = (1920, 1080)
VIDEO_OUTPUT_NAME = "video_record.mp4"
FOUR_CHAR_CODE = cv.VideoWriter_fourcc(*"mp4v")
writer = cv.VideoWriter(VIDEO_OUTPUT_NAME, FOUR_CHAR_CODE, FPS, (SCREENSIZE))

thread3 = threading.Thread(target=record_audio, daemon=True, name="audio").start()

#Main Loop
while not stop_:
    #Store Video
    img = pyautogui.screenshot()
    frame = np.array(img)
    #Convert Frame color
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    writer.write(rgb_frame)
    #Pause Logic
    if pause_:
        while pause_:
            pass
#Saving and Writing
writer.release()


#Merging all togheter
video = ffmpeg.input(VIDEO_OUTPUT_NAME)
audio = ffmpeg.input(A_OUTPUT_FILENAME)
out = ffmpeg.output(video, audio, 'v.mp4', vcodec='copy', acodec='aac', strict='experimental')
out.run()
#Exit
sys.exit()