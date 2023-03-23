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
def initIdx():
    global new_idx
    new_idx = 0
    return new_idx

def getIdx():
    global new_idx
    return new_idx

def setPause(val):
    global isPause
    isPause = val
    return isPause

def getPause():
    global isPause
    return isPause

# val = True / False
def setFinish(val):
    global isFinish
    isFinish = val
    if isFinish == True:
        initIdx()
        setPause(False)
    return isFinish

def getFinish():
    global isFinish
    return isFinish

# 이전 버튼 눌렀을 때
def prevBox(win, p1, p2, p3, p4, logpath, tF, tT, idx):
    global new_idx
    global img_copy_11_except, img_copy_12_except, img_copy_13_except, img_copy_14_except
    global img_copy_11_draw, img_copy_12_draw, img_copy_13_draw, img_copy_14_draw
    global isExcept
    global isFinish
    global isPause

    color_valid = (0, 255, 0)
    color_ex = (0, 0, 255)

    analysis = readLog(logpath)

    analyze = analysis[idx - 1]
    new_idx = idx - 1

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

    if isExcept:
        print("isExcept: ", isExcept)
        img_copy_11 = img_copy_11_except.copy()
        img_copy_12 = img_copy_12_except.copy()
        img_copy_13 = img_copy_13_except.copy()
        img_copy_14 = img_copy_14_except.copy()
    
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

    win.update()

# 이후 버튼 눌렀을 때
def nextBox(win, p1, p2, p3, p4, logpath, tF, tT, idx):
    global new_idx
    global img_copy_11_except, img_copy_12_except, img_copy_13_except, img_copy_14_except
    global img_copy_11_draw, img_copy_12_draw, img_copy_13_draw, img_copy_14_draw
    global isExcept
    global isFinish
    global isPause

    color_valid = (0, 255, 0)
    color_ex = (0, 0, 255)

    analysis = readLog(logpath)

    analyze = analysis[idx + 1]
    new_idx = idx + 1

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

    if isExcept:
        print("isExcept: ", isExcept)
        img_copy_11 = img_copy_11_except.copy()
        img_copy_12 = img_copy_12_except.copy()
        img_copy_13 = img_copy_13_except.copy()
        img_copy_14 = img_copy_14_except.copy()
    
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

    win.update()

# 재생 버튼 눌렀을 때
img_copy_11_except = None
img_copy_12_except = None
img_copy_13_except = None
img_copy_14_except = None
img_copy_11_draw = None
img_copy_12_draw = None
img_copy_13_draw = None
img_copy_14_draw = None
isFinish = False
isPause = False
def drawBox(win, p1, p2, p3, p4, logpath, tF, tT, idx, speed):
    global new_idx
    global img_copy_11_except, img_copy_12_except, img_copy_13_except, img_copy_14_except
    global img_copy_11_draw, img_copy_12_draw, img_copy_13_draw, img_copy_14_draw
    global isExcept
    global isFinish
    global isPause

    color_valid = (0, 255, 0)
    color_ex = (0, 0, 255)

    analysis = readLog(logpath)

    img_copy_11 = p1.img.copy()
    img_copy_12 = p2.img.copy()
    img_copy_13 = p3.img.copy()
    img_copy_14 = p4.img.copy()

    if getPause():
        setPause(False)
    else:
        img_copy_11_except = p1.img.copy()
        img_copy_12_except = p2.img.copy()
        img_copy_13_except = p3.img.copy()
        img_copy_14_except = p4.img.copy()

    img_copy_11_draw = p1.img.copy()
    img_copy_12_draw = p2.img.copy()
    img_copy_13_draw = p3.img.copy()
    img_copy_14_draw = p4.img.copy()

    for i in range(idx, len(analysis)):
        analyze = analysis[i]
        new_idx = i

        if isExcept:
            print("isExcept: ", isExcept)
            img_copy_11 = img_copy_11_except.copy()
            img_copy_12 = img_copy_12_except.copy()
            img_copy_13 = img_copy_13_except.copy()
            img_copy_14 = img_copy_14_except.copy()
        else:
            print("isExcept: ", isExcept)
            img_copy_11 = img_copy_11_draw.copy()
            img_copy_12 = img_copy_12_draw.copy()
            img_copy_13 = img_copy_13_draw.copy()
            img_copy_14 = img_copy_14_draw.copy()


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

        time.sleep(-time.time() % (speed / 100))

        win.update()
    
    messagebox.showinfo(title="End of Log File", message="END OF LOG FILE: 로그 재생이 끝났습니다.")
    print("Log Finished")
    isFinish = True
    setFinish(isFinish)

# dID11, dID12, dID13, dID14는 str
isExcept = False
def setIsExcept(val):
    global isExcept
    isExcept = val
    return isExcept

def getIsExcept():
    global isExcept
    return isExcept

def drawExcept(win, p1, p2, p3, p4, isShow):
    color_ex = (255, 255, 0, 128)
    global img_copy_11_except, img_copy_12_except, img_copy_13_except, img_copy_14_except
    global img_copy_11_draw, img_copy_12_draw, img_copy_13_draw, img_copy_14_draw
    global isExcept

    dID11 = str(p1.deviceID)
    dID12 = str(p2.deviceID)
    dID13 = str(p3.deviceID)
    dID14 = str(p4.deviceID)

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
            ''' 예외구역 박스에 투명한 색 채워넣기 '''
            # alpha_channel11 = np.zeros(img_copy_11_except.shape[:2], dtype=np.uint8)
            # cv2.fillPoly(alpha_channel11, [np.int32(d)], 255)
            # img_copy_11_except = cv2.merge(img_copy_11_except, alpha_channel11)
            # cv2.polylines(img_copy_11_except, np.int32([d]), True, color_ex, 2)
            # img_copy_11_except = img_copy_11_except[:, :, :3]
            cv2.polylines(img_copy_11_except, np.int32([d]), True, color_ex, 2)

        for d in drawData12:
            ''' 예외구역 박스에 투명한 색 채워넣기 '''
            # alpha_channel12 = np.zeros(img_copy_12_except.shape[:2], dtype=np.uint8)
            # cv2.fillPoly(alpha_channel12, [np.int32(d)], 255)
            # img_copy_12_except = cv2.merge(img_copy_12_except, alpha_channel12)
            # cv2.polylines(img_copy_12_except, np.int32([d]), True, color_ex, 2)
            # img_copy_12_except = img_copy_12_except[:, :, :3]
            cv2.polylines(img_copy_12_except, np.int32([d]), True, color_ex, 2)

        for d in drawData13:
            ''' 예외구역 박스에 투명한 색 채워넣기 '''
            # alpha_channel13 = np.zeros(img_copy_13_except.shape[:2], dtype=np.uint8)
            # cv2.fillPoly(alpha_channel13, [np.int32(d)], 255)
            # img_copy_13_except = cv2.merge(img_copy_13_except, alpha_channel13)
            # cv2.polylines(img_copy_13_except, np.int32([d]), True, color_ex, 2)
            # img_copy_13_except = img_copy_13_except[:, :, :3]
            cv2.polylines(img_copy_13_except, np.int32([d]), True, color_ex, 2)

        for d in drawData14:
            ''' 예외구역 박스에 투명한 색 채워넣기 '''
            # alpha_channel14 = np.zeros(img_copy_14_except.shape[:2], dtype=np.uint8)
            # cv2.fillPoly(alpha_channel14, [np.int32(d)], 255)
            # img_copy_14_except = cv2.merge(img_copy_14_except, alpha_channel14)
            # cv2.polylines(img_copy_14_except, np.int32([d]), True, color_ex, 2)
            # img_copy_14_except = img_copy_14_except[:, :, :3]
            cv2.polylines(img_copy_14_except, np.int32([d]), True, color_ex, 2)
    
    if isShow == 1:
        isExcept = True
        drawExceptHelper(img_copy_11_except, img_copy_12_except, img_copy_13_except, img_copy_14_except, p1, p2, p3, p4)
    else:
        isExcept = False
        drawExceptHelper(img_copy_11_draw, img_copy_12_draw, img_copy_13_draw, img_copy_14_draw, p1, p2, p3, p4)

    win.update()

def drawExceptHelper(i11, i12, i13, i14, p1, p2, p3, p4):
    img11 = cv2.cvtColor(i11, cv2.COLOR_BGR2RGB)
    img12 = cv2.cvtColor(i12, cv2.COLOR_BGR2RGB)
    img13 = cv2.cvtColor(i13, cv2.COLOR_BGR2RGB)
    img14 = cv2.cvtColor(i14, cv2.COLOR_BGR2RGB)

    img11_pil = Image.fromarray(img11)
    img12_pil = Image.fromarray(img12)
    img13_pil = Image.fromarray(img13)
    img14_pil = Image.fromarray(img14)

    img11_tk = ImageTk.PhotoImage(img11_pil)
    img12_tk = ImageTk.PhotoImage(img12_pil)
    img13_tk = ImageTk.PhotoImage(img13_pil)
    img14_tk = ImageTk.PhotoImage(img14_pil)

    p1.img_tk = img11_tk
    p2.img_tk = img12_tk
    p3.img_tk = img13_tk
    p4.img_tk = img14_tk

    p1.label.configure(image=p1.img_tk)
    p2.label.configure(image=p2.img_tk)
    p3.label.configure(image=p3.img_tk)
    p4.label.configure(image=p4.img_tk)

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