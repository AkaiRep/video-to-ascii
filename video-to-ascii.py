import os
import pygame
import cv2
from time import sleep as sleep
from PIL import Image
lines = 140
columns = 70

vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 1

os.system("mode con cols=140 lines=70")
scale=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,   ")
scale.reverse()
number = 1
# pygame.mixer.init()
# pygame.mixer.music.load("b.mp3")
# pygame.mixer.music.play()
while True:
    cv2.imwrite("image"+str(number)+".jpg",image)     # save frame as JPEG file    
    success,image = vidcap.read()
    im = Image.open('image'+str(number)+'.jpg')
    im = im.resize((lines, columns))
    im = im.convert('L')
    pix = im.load()
    result=[]
    x,y=1,1
    while y < columns:
        x=1
        while x < lines:
            result.append(scale[int(pix[x,y]/36)-1]);x+=1
        result.append('\n');y+=1
    print(''.join(result))
    os.remove("image"+str(number)+".jpg")
    number+=1
    
    count+=1
    
    
    sleep(0.0016)
    
