import os
from time import sleep as sleep

import glob
import cv2
from PIL import Image


columns,lines = 140,70
rev = True

os.system('cls')
os.system('mode con cols=40 lines=20 ')
selected_video_number = 0

videos = glob.glob('*.mp4')

for video_index, video_name in enumerate(videos):
    print(f'[{video_index + 1}] - {video_name}')

selected_video_number = input('\nВведите номер видео: ')

try:
    selected_video = videos[int(selected_video_number) - 1]
except:
    os.system('mode con cols=100 lines=30 ')
    print(f'{selected_video_number} - неверный номер X_X')
    exit()

vidcap = cv2.VideoCapture(selected_video)
success, image = vidcap.read()

os.system(f'mode con cols={columns} lines={lines}')
symbols = list(r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,   ')

if rev:
    symbols.reverse()

try:
    while True:
        success, image = vidcap.read()
        im = Image.fromarray(image)
        im = im.resize((columns, lines))
        im = im.convert('L')
        pixels = im.load()
        result = []

        for y in range(1, lines):
            for x in range(1, columns):
                result.append(symbols[int(pixels[x, y] / 36) - 1])
            result.append('\n')

        print(''.join(result))

        sleep(0.016)
except KeyboardInterrupt:
    os.system("mode con cols=100 lines=30 ")