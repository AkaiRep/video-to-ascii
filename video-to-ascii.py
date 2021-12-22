import os
from time import sleep as sleep

import glob
import cv2
from PIL import Image


video_columns, video_lines = 140, 70
rev = True

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
    selected_video = videos[int(selected_video_number) - 1]
except:
    set_console_size(100, 30)
    print(f'{selected_video_number} - неверный номер X_X')
    exit()

vidcap = cv2.VideoCapture(selected_video)
success, image = vidcap.read()

set_console_size(video_columns, video_lines)
symbols = list(r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,   ')

if rev:
    symbols.reverse()

try:
    while True:
        success, image = vidcap.read()
        
        if not success:
            break

        im = Image.fromarray(image)
        im = im.resize((video_columns, video_lines))
        im = im.convert('L')
        pixels = im.load()
        result = []

        for y in range(1, video_lines):
            for x in range(1, video_columns):
                result.append(symbols[int(pixels[x, y] / 36) - 1])
            result.append('\n')

        print(''.join(result))

        sleep(0.016)
except KeyboardInterrupt:
    set_console_size(100, 30)