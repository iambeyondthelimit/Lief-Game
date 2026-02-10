import os 
import time
import sys


def animate(text, speed=0.04):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep (speed)
        
def input_animation(text, speed=0.05):
    animate(text, speed)
    return input("\n> ").strip()
        
def clear(speed=1):
        time.sleep (speed)
        os.system("clear")
        
def backstep(backward, speed=0.01):
    time.sleep(0.30)
    for b in backward:
        print("\b \b", end="", flush = True)
        time.sleep (speed)
        
    
