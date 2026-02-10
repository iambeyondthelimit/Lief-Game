import os 
import time
import sys


def animate(text, speed=0.05):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep (speed)
        
def input_animation(text, speed=0.05):
    animate(text, speed)
    return input("\n: ").strip()
        
def clear():
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
