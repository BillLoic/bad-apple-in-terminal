import cv2
import time
import os
import signal
import sys
import subprocess
import numpy as np

def cleanup():
    print("\033[0m\033[?25h\033[2J\033[H")  # Reset colors, show cursor, clear screen
    os._exit(0)

def signal_handler(sig, frame):
    cleanup()
    
proc = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "bad_apple.aac"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if not proc.pid:
    print("ffplay error. Please install ffmpeg to play audio.")
    os._exit(1)

# Hide cursor and clear screen
print("\033[?25l\033[2J", end='')

def main():
    try:
        video = cv2.VideoCapture("bad_apple.mp4")
        fps = video.get(cv2.CAP_PROP_FPS)
        spf = 1 / fps

        while True:
            ret, frame = video.read()
            if not ret:
                break
                
            output = "\033[H"  # Move cursor to top-left
            for row in frame:
                for pixel in row:
                    if all(pixel <= [128, 128, 128]):
                        output += " "
                    else:
                        output += "\u2588"  # Full block character
                output += "\n"  # New line after each row
                
            print("\r" + output, end='', flush=True)
            time.sleep(spf - 0.012)

    except KeyboardInterrupt:
        proc.kill()
        cleanup()
        video.release()

if __name__ == "__main__":
    main()
    cleanup()