import time
import os
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
        with open("frames_black_ver.txt", "r") as frames_file:
            frames = frames_file.read().split("\n\n\n")
            del frames[-1]
            for frame in frames:
                output = "\033[H"
                print("\r" + output + frame, end='', flush=True)
                time.sleep(0.033)

    except KeyboardInterrupt:
        proc.kill()
        cleanup()

if __name__ == "__main__":
    main()
    cleanup()