import cv2
import numpy as np
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from PIL import ImageDraw as Dr

from readExcept import *
from readLog import *

new_idx = 0
def getIdx():
    global new_idx
    print("new_idx = ", new_idx)
    return new_idx

# 이전 버튼 눌렀을 때
def prevBox(win, p1, p2, p3, p4, logpath, tF, tT, idx):
    return

# 이후 버튼 눌렀을 때
def nextBox(win, p1, p2, p3, p4, logpath, tF, tT, idx):
    return

# 재생 버튼 눌렀을 때
def drawBox(win, p1, p2, p3, p4, logpath, tF, tT, idx, speed):
# def drawBox(img, analysis, dID, tF, tT, curr):
    global new_idx

    x, y, w, h = 0, 0, 0, 0
    obj = None

    color_valid = (0, 255, 0)
    color_ex = (0, 0, 255)

    analysis = readLog(logpath)

    for i in range(idx, len(analysis)):
        analyze = analysis[i]
        new_idx = i

        img_copy_11 = p1.img.copy()
        img_copy_12 = p2.img.copy()
        img_copy_13 = p3.img.copy()
        img_copy_14 = p4.img.copy()

        dID11 = str(p1.deviceID)
        dID12 = str(p2.deviceID)
        dID13 = str(p3.deviceID)
        dID14 = str(p4.deviceID)

        # 1회 분석의 값들이 다 리스트 형태, 순서는 다 같음
        _, allTime = getTime(analyze)
        box = getBox(analyze)
        obj = getObject(analyze)
        dID = getDeviceID(analyze)
        valid = isValid(analyze)
        
        for j in range(len(analyze)):
            x = box[j][0]
            y = box[j][1]
            w = box[j][2]
            h = box[j][3]

            if allTime[j] > tF and allTime[j] < tT:
                if dID[j] == dID11:
                    print(analyze[j])
                    if valid[j] == "VALID":
                        cv2.putText(img_copy_11, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_valid, 2)
                        cv2.rectangle(img_copy_11, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                    if valid[j] == "EX":
                        cv2.putText(img_copy_11, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_ex, 2)
                        cv2.rectangle(img_copy_11, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)

                if dID[j] == dID12:
                    print(analyze[j])
                    if valid[j] == "VALID":
                        cv2.putText(img_copy_12, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_valid, 2)
                        cv2.rectangle(img_copy_12, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                    if valid[j] == "EX":
                        cv2.putText(img_copy_12, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_ex, 2)
                        cv2.rectangle(img_copy_12, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)

                if dID[j] == dID13:
                    print(analyze[j])
                    if valid[j] == "VALID":
                        cv2.putText(img_copy_13, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_valid, 2)
                        cv2.rectangle(img_copy_13, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                    if valid[j] == "EX":
                        cv2.putText(img_copy_13, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_ex, 2)
                        cv2.rectangle(img_copy_13, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)

                if dID[j] == dID14:
                    print(analyze[j])
                    if valid[j] == "VALID":
                        cv2.putText(img_copy_14, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_valid, 2)
                        cv2.rectangle(img_copy_14, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_valid, 2)
                    if valid[j] == "EX":
                        cv2.putText(img_copy_14, obj[j], (x // 3, y // 3), cv2.FONT_HERSHEY_COMPLEX, 0.7, color_ex, 2)
                        cv2.rectangle(img_copy_14, (x // 3, y // 3), ((x + w) // 3, (y + h) // 3), color_ex, 2)

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

        time.sleep(-time.time() % speed)

        win.update()
    
    messagebox.showinfo(title="End of Log File", message="END OF LOG FILE: 로그 재생이 끝났습니다.")

def drawExcept(win, p1, p2, p3, p4, isShow):
    color_ex = (0, 0, 255)

    img_copy_11 = p1.img.copy()
    img_copy_12 = p2.img.copy()
    img_copy_13 = p3.img.copy()
    img_copy_14 = p4.img.copy()

    dID11 = p1.deviceID
    dID12 = p2.deviceID
    dID13 = p3.deviceID
    dID14 = p4.deviceID

    coord11 = getRegion(dID11)
    coord12 = getRegion(dID12)
    coord13 = getRegion(dID13)
    coord14 = getRegion(dID14)

    pnt_datas11 = pnt2draw(coord11)
    pnt_datas12 = pnt2draw(coord12)
    pnt_datas13 = pnt2draw(coord13)
    pnt_datas14 = pnt2draw(coord14)

    if isShow == 1:
        drawData11 = []
        drawData12 = []
        drawData13 = []
        drawData14 = []

        for shape in pnt_datas11:
            t = []
            for pnt in shape:
                t.append([int(pnt[0] / 3), int(pnt[1] / 3)])
            drawData11.append(t)

        for shape in pnt_datas12:
            t = []
            for pnt in shape:
                t.append([int(pnt[0] / 3), int(pnt[1] / 3)])
            drawData12.append(t)

        for shape in pnt_datas13:
            t = []
            for pnt in shape:
                t.append([int(pnt[0] / 3), int(pnt[1] / 3)])
            drawData13.append(t)

        for shape in pnt_datas14:
            t = []
            for pnt in shape:
                t.append([int(pnt[0] / 3), int(pnt[1] / 3)])
            drawData14.append(t)

        for d in drawData11:
            cv2.polylines(img_copy_11, np.int32([d]), True, color_ex, 2)

        for d in drawData12:
            cv2.polylines(img_copy_12, np.int32([d]), True, color_ex, 2)

        for d in drawData13:
            cv2.polylines(img_copy_13, np.int32([d]), True, color_ex, 2)

        for d in drawData14:
            cv2.polylines(img_copy_14, np.int32([d]), True, color_ex, 2)
        
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