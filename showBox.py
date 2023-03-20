import cv2
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from readLog import *
from readExcept import *

class ImagePlayer:
    def __init__(self, win, imgPath, deviceID, idx, each_analyze):
        self.win = win
        self.imgPath = imgPath
        self.deviceID = deviceID
        self.idx = idx
        self.each_analyze = each_analyze

        self.label = Label(self.win)
        self.label.pack(side="left", padx=10)

        self.img = cv2.imread(self.imgPath)
        self.img = cv2.resize(self.img, (360, 640))

        self.img_pil = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        self.img_tk = ImageTk.PhotoImage(self.img_pil)

        self.label.config(image=self.img_tk)

    def showBox(self, logPath, dID, tF, tT, btn, curr):

        x, y, w, h = 0, 0, 0, 0
        obj = None

        color_valid = (0, 255, 0)
        color_ex = (0, 0, 255)

        analysis = readLog(logPath)

        # data는 item[i] -> 1회 분석의 각각의 아이템
        # 재귀를 이용해서 사용
        def recurBox(data):
            cvimg = self.img.copy()

            _, iTime = getTime(data)
            x, y, w, h = getBox(data)
            obj = getObject(data)

            if iTime > tF and iTime < tT:
                if isValid(data):
                    cvimg = cv2.rectangle(cvimg, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 3)
                else:
                    cvimg = cv2.rectangle(cvimg, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 3)

                new_img_pil = Image.fromarray(cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB))
                new_img_tk = ImageTk.PhotoImage(new_img_pil)

                self.img_tk.paste(new_img_tk)
                self.label.configure(image=self.img_tk)
        '''
        TODO
        ***Find out if this code works***
        '''
        # Version 1
        # for i in range(curr, len(analysis)):
        #     self.idx = i
        #     for j in range (len(analysis[i])):
        #         self.each_analyze = j
        #         if str(dID) == getDeviceID(analysis[i][j]):
        #             self.win.after(10, recurBox(analysis[i][j]))

        # Version 2 - while loop으로 바꾸기
        while btn != "btn finish":
            if btn == "btn play":
                pass
            elif btn == "btn pause":
                pass
            elif btn == "btn back":
                pass
            elif btn == "btn next":
                pass
            elif btn == "btn stop":
                self.idx = 0
                self.each_analyze = 0


    def drawExcept(self, dID):
        coord = getRegion(dID)
        pnt_datas = pnt2draw(coord)
        color_ex = (0, 0, 255)

        drawData = []
        for shape in pnt_datas:
            t = []
            for pnt in shape:
                t.append([int(pnt[0] / 3), int(pnt[1] / 3)])
            drawData.append(t)

        for d in drawData:
            self.img = cv2.polylines(self.img, np.int32([d]), True, color_ex, 2)