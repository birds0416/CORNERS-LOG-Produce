import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from readLog import *
from readExcept import *

class ImagePlayer:
    def __init__(self, win, imgPath, deviceID):
        self.win = win
        self.imgPath = imgPath
        self.deviceID = deviceID

        self.label = Label(self.win)
        self.label.pack(side="left", padx=10)

        self.img = cv2.imread(self.imgPath)
        self.img = cv2.resize(self.img, (360, 640))

        self.img_pil = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        self.img_tk = ImageTk.PhotoImage(self.img_pil)

        self.label.config(image=self.img_tk)

    def showBox(self, logPath, dID):

        x, y, w, h = 0, 0, 0, 0
        obj = None
        new_img = self.img

        color_valid = (0, 255, 0)
        color_ex = (0, 0, 255)

        analysis = readLog(logPath)
        for item in analysis:
            for i in range (len(item)):
                if str(dID) == getDeviceID(item[i]):
                    x, y, w, h = getBox(item[i])
                    obj = getObject(item[i])

                    if isValid(item[i]):
                        new_img = cv2.rectangle(new_img, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 3)
                    else:
                        new_img = cv2.rectangle(new_img, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 3)
                    
                    new_img_pil = Image.fromarray(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
                    new_img_tk = ImageTk.PhotoImage(new_img_pil)

                    self.img_tk = new_img_tk
                    self.label.configure(image=self.img_tk)
                    
                # self.win.after(10, self.showBox())