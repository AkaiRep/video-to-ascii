import os
import glob
import cv2
from time import sleep as sleep
from PIL import Image
columns,lines = 140,70;rev=True
os.system("cls")
os.system("mode con cols=40 lines=20 ");y=0
videos=glob.glob("*.mp4")
while y<len(videos):print("["+str(y+1)+"] - "+videos[y]);y+=1
cmd = input("\nВведите номер видео: ")
try:cmd = videos[int(cmd)-1]
except:os.system("mode con cols=100 lines=30 ");print(cmd+' - неверный номер X_X');exit()
vidcap = cv2.VideoCapture(cmd)
success,image = vidcap.read();dele,number,count = 1,1,1 
os.system("mode con cols="+str(columns)+" lines="+str(lines))
scale=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,   ")
if rev:scale.reverse()
try:
    while True:
        success,image = vidcap.read()
        im = Image.fromarray(image)
        im = im.resize((columns, lines))
        im = im.convert('L')
        pix = im.load()
        result=[]
        x,y=1,1
        while y < lines:
            x=1
            while x < columns:result.append(scale[int(pix[x,y]/36)-1]);x+=1
            result.append('\n');y+=1
        print(''.join(result))
        number+=1;count+=1;sleep(0.016)
except KeyboardInterrupt:os.system("mode con cols=100 lines=30 ")