import threading
from time import sleep
import keyboard
import sys
pausa_ = True
def changepause():
    global pausa_
    while True:
        if keyboard.is_pressed('o'):
            pausa_ = not pausa_
            sys.exit()


t = threading.Thread(target=changepause).start()

while pausa_:
    print('inside loop')
    sleep(0.5)

sys.exit()