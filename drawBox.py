import cv2
import numpy as np
import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageDraw as Dr

from readExcept import *
from readLog import *

def drawBox(win, p1, p2, p3, p4, logpath, tF, tT):
# def drawBox(img, analysis, dID, tF, tT, curr):
    x, y, w, h = 0, 0, 0, 0
    obj = None
    img_copy_tk = None

    analysis = readLog(logpath)

    color_valid = (0, 255, 0)
    color_ex = (0, 0, 255)

    i = 0
    j = 0

    while True:
        # cv2.imshow("image" + str(dID), img)
        idx = i

        analyze = analysis[i]
        maxJ = len(analyze)

        eData = analyze[j]

        img_copy_11 = p1.img.copy()
        img_copy_12 = p2.img.copy()
        img_copy_13 = p3.img.copy()
        img_copy_14 = p4.img.copy()

        dID11 = str(p1.deviceID)
        dID12 = str(p2.deviceID)
        dID13 = str(p3.deviceID)
        dID14 = str(p4.deviceID)

        _, eTime = getTime(eData)
        x, y, w, h = getBox(eData)
        obj = getObject(eData)
        ID = getDeviceID(eData)

        if eTime > tF and eTime < tT:
            if ID == dID11:
                print(eData)
                if isValid(eData):
                    cv2.rectangle(img_copy_11, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                else:
                    cv2.rectangle(img_copy_11, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)
                # cv2.imshow("image" + ID , img_copy)

            if ID == dID12:
                print(eData)
                if isValid(eData):
                    cv2.rectangle(img_copy_12, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                else:
                    cv2.rectangle(img_copy_12, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)
                # cv2.imshow("image" + ID , img_copy)

            if ID == dID13:
                print(eData)
                if isValid(eData):
                    cv2.rectangle(img_copy_13, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                else:
                    cv2.rectangle(img_copy_13, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)
                # cv2.imshow("image" + ID , img_copy)

            if ID == dID14:
                print(eData)
                if isValid(eData):
                    cv2.rectangle(img_copy_14, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                else:
                    cv2.rectangle(img_copy_14, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)
                # cv2.imshow("image" + ID , img_copy)

            img_copy_11 = cv2.cvtColor(img_copy_11, cv2.COLOR_BGR2RGB)
            img_copy_12 = cv2.cvtColor(img_copy_12, cv2.COLOR_BGR2RGB)
            img_copy_13 = cv2.cvtColor(img_copy_13, cv2.COLOR_BGR2RGB)
            img_copy_14 = cv2.cvtColor(img_copy_14, cv2.COLOR_BGR2RGB)

            img_copy_11_pil = Image.fromarray(img_copy_11)
            img_copy_12_pil = Image.fromarray(img_copy_12)
            img_copy_13_pil = Image.fromarray(img_copy_13)
            img_copy_14_pil = Image.fromarray(img_copy_14)

            img_copy_11_tk = ImageTk.PhotoImage(img_copy_11_pil)
            img_copy_12_tk = ImageTk.PhotoImage(img_copy_12_pil)
            img_copy_13_tk = ImageTk.PhotoImage(img_copy_13_pil)
            img_copy_14_tk = ImageTk.PhotoImage(img_copy_14_pil)

            p1.img_tk = img_copy_11_tk
            p2.img_tk = img_copy_12_tk
            p3.img_tk = img_copy_13_tk
            p4.img_tk = img_copy_14_tk

            p1.label.configure(image=p1.img_tk)
            p2.label.configure(image=p2.img_tk)
            p3.label.configure(image=p3.img_tk)
            p4.label.configure(image=p4.img_tk)

            win.update()

        if j < maxJ - 1:
            j += 1
        else:
            i += 1
            j = 0
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            cv2.destroyAllWindows()
            break
    
    return idx, img_copy_tk

''' drawBox Test '''
# img1 = cv2.imread("C:/Users/USER/Desktop/Programs/Corners_programs/pythontools/device_image/NIPA_11_20230321102221972.jpg")
# img2 = cv2.imread("C:/Users/USER/Desktop/Programs/Corners_programs/pythontools/device_image/NIPA_12_20230321093507232.jpg")
# img3 = cv2.imread("C:/Users/USER/Desktop/Programs/Corners_programs/pythontools/device_image/NIPA_13_20230321102332611.jpg")
# img4 = cv2.imread("C:/Users/USER/Desktop/Programs/Corners_programs/pythontools/device_image/NIPA_14_20230321093529152.jpg")

# img1 = cv2.resize(img1, (360, 640))
# img2 = cv2.resize(img2, (360, 640))
# img3 = cv2.resize(img3, (360, 640))
# img4 = cv2.resize(img4, (360, 640))

# logpath = "C:/Users/USER/Desktop/Programs/Corners_programs/pythontools/대상WL 로그재현 Tool/log/DetectManager20230317.log"
# analysis = readLog(logpath)

# timeF = datetime.strptime("08:30:00", "%H:%M:%S").time()
# timeT = datetime.strptime("09:33:00", "%H:%M:%S").time()

# drawBox(img1, analysis, 11, timeF, timeT, 0)
# drawBox(img2, analysis, 12, timeF, timeT, 0)
# drawBox(img3, analysis, 13, timeF, timeT, 0)
# drawBox(img4, analysis, 14, timeF, timeT, 0)