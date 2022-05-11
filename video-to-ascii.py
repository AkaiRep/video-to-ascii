import os
import sys
from time import sleep as sleep

import glob
import cv2
from PIL import Image

ESC = b'\033'
CSI = ESC + b'['

# Linux and new Windows supports ANSI Escape Sequences
use_ansi_escape_sequences = True

if not use_ansi_escape_sequences:
    import ctypes
    from ctypes import c_long

    console_handle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))

video_columns, video_lines = 140, 70

def set_console_size(columns, lines):
    os.system(f'mode con cols={columns} lines={lines} ')


os.system('cls')
set_console_size(40, 20)
selected_video_number = 0

videos = glob.glob('*.mp4')

for video_index, video_name in enumerate(videos):
    print(f'[{video_index + 1}] - {video_name}')

selected_video_number = input('\nВведите номер видео: ')

try:
    fps = int(input("Required FPS:"))
    has_inverted_colors = bool(input("Inverted colors?(True:False):"))
    loop = bool(input("Loop Video?(True:False):"))
except:
    fps = 30
    has_inverted_colors = True
    loop = False

try:
    selected_video = videos[int(selected_video_number) - 1]
except:
    set_console_size(100, 30)
    print(f'{selected_video_number} - неверный номер X_X')
    exit()

vidcap = cv2.VideoCapture(selected_video)
success, image = vidcap.read()

set_console_size(video_columns, video_lines)
symbols = list(r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,   ')

if has_inverted_colors:
    symbols.reverse()

stdout = os.fdopen(sys.stdout.fileno(), 'wb', video_columns * video_lines * 2)

try:
    while True:
        success, image = vidcap.read()
        #Loop video if end reached
        if not success and loop:
            vidcap.open(selected_video)
                continue

        im = Image.fromarray(image)
        im = im.resize((video_columns, video_lines))
        im = im.convert('L')
        pixels = im.load()
        result = []

        for y in range(1, video_lines):
            for x in range(1, video_columns):
                result.append(symbols[int(pixels[x, y] / 36) - 1])
            result.append('\n')

        # Set cursor to the top left corner
        if use_ansi_escape_sequences:
            stdout.write(CSI + b'1;1H')
        else:
            ctypes.windll.kernel32.SetConsoleCursorPosition(console_handle, 0)
        
        stdout.write(''.join(result).encode())
        stdout.flush()

        sleep(1 / fps)
except KeyboardInterrupt:
    set_console_size(100, 30)
