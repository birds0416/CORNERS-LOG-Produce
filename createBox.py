import cv2
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageDraw as Dr
from time import sleep

from readLog import *
from readExcept import *
from drawBox import *

class ImagePlayer:
    def __init__(self, win, imgPath, deviceID, idx):
        self.win = win
        self.imgPath = imgPath
        self.deviceID = deviceID
        self.idx = idx

        self.contain0 = Frame(self.win)
        self.contain0.pack(side="left", anchor=NW, padx=(10, 0))

        self.nameID = Label(self.contain0, text=str(deviceID), font=('Arial', 12))
        self.nameID.pack(side="left", padx=(10, 0))

        self.contain1 = Frame(self.win)
        self.contain1.pack(side="left", anchor=NW, padx=10)

        self.label = Label(self.contain1)
        self.label.pack(side="left", padx=10)

        self.img = cv2.imread(self.imgPath)
        self.img = cv2.resize(self.img, (360, 640))

        self.img_pil = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        self.img_tk = ImageTk.PhotoImage(self.img_pil)

        self.label.config(image=self.img_tk)
