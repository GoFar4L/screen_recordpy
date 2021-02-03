import pyaudio
import wave
import threading


class AudioRecord():
    def __init__(self, outputName):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.WAVE_OUTPUT_FILENAME = outputName
        self.audio = pyaudio.PyAudio()
        self.frames = []
        self.isRunning = False
        self.isPaused = False
        self.stream = None
        print('Audio Record setted up')

    def record(self):
        try:    
            print('Device info: ')
            print(pyaudio.)
            print('Start Audio Recording')   
            self.isRunning = True
            self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
            while self.isRunning:
                if self.isPaused:
                    print('Audio Paused')
                    self.stream.stop_stream()
                    while self.isPaused:
                        pass
                    self.stream.start_stream()
                    print('Audio Resumed')           
                data = self.stream.read(self.CHUNK)
                self.frames.append(data)

            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
            waveFile.setnchannels(self.CHANNELS)
            waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            waveFile.setframerate(self.RATE)
            waveFile.writeframes(b''.join(self.frames))
            waveFile.close()
            print('Audio Record Ended')
            return True
        except:
            return False


    
    
    