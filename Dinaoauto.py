
"""
Created on Mon May  4 12:27:42 2020

@author: Pranav
"""
#play at 400%

import time
from PIL import ImageGrab
import pyautogui

def makemove(data):
    count=0
    cnt=0
    # for i in range(10,40):
    #     for j in range(100,120):
    #        data[i,j]=255
    # if data[10,120] > 150:
    #     print(data[10,120])
    if data[10,120] > 150:
        for i in range(580,590):
            for j in range(520,571):
                # data[i,j] = 0
                # data[i,j] = 0
                if data[i,j] < 100 and data[i,j] > 10:
                    count+=1
                    # pyautogui.press("up")
                    if count==1:
                        pyautogui.keyDown("up")
                    break
                    
                
        for i in range(370,411):
            for j in range(400,450):
                # data[i,j] = 0
                if  data[i,j]<100 and data[i,j] > 10:
                    cnt+=1
                    # pyautogui.press("down")
                    if count==1:
                        #  pyautogui.keyDown("down")
                        #  time.sleep(.6)
                       pyautogui.keyDown("down")
                    # pyautogui.keyDown("down")
                    # time.sleep(.4)
                    break
    else:
        for i in range(580,601):
            for j in range(520,571):
                # data[i,j] = 200
                if data[i,j] > 100:
                    count+=1
                    if count==1:
                        pyautogui.keyDown("up")
                    # if count==1:
                    #     pyautogui.press("up") 
                    break
                    
                
        for i in range(370,411):
            for j in range(400,450):
                # data[i,j] = 200
                
                if  data[i,j]>100:
                    cnt+=1
                    if count==1:
                        pyautogui.keyDown("down")
                    # if count==1:
                    #     pyautogui.press("up")
                        #  time.sleep(.6)
                        # pyautogui.press("up")
                    # pyautogui.keyDown("down")
                    # time.sleep(.4)
                    
                    break
        
      
       
    return
if __name__=='__main__':
    print("Game starts in 4 seconds")
    time.sleep(3)
    pyautogui.keyDown("up")
    # pyautogui.keyDown("down")
    # time.sleep(.4)
    # pyautogui.keyUp("down")
    
    count=0
    while 1:
        count+=1
        img = ImageGrab.grab().convert('L')
        data = img.load()
        makemove(data)
        # for i in range(370,411):
        #     for j in range(400,460):
        #         data[i,j] = 150
        # for i in range(10,60):
        #     for j in range(100,150):
        # #         data[i,j] = 150
        # img.show()
        # if count==1:
        #     break;
        img.close()
        # time.sleep(12)
         # i in range(450,545):
         #    for j in range(450,500)
        # for i in range(440,451):
        #     for j in range(520,531):
        #         data[i,j] = 150