import cv2
import numpy as np
import pandas as pd
import os
import os.path
import json

# import from local py
from readLog import *
from readExcept import *
from createBox import *

# Import Tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import ImageTk, Image

#Create an instance of Tkinter frame
win= Tk()
win.title("대상WL 로그재현 Tool")
#Set the geometry of Tkinter frame
win.geometry("900x400")
win.protocol('WM_DELETE_WINDOW', lambda: onclose(win))


'''
TODO
* ---로그파일 불러와서 읽기
* 하단 버튼 기능 전부 구현
* ---이미지 경로 tkinter 윈도우에 4개 연속으로 띄워서 박스 그리기
'''

# 이미지 경로 저장
imgPathList = ["", "", "", ""]

# 이미지 경로 텍스트 파일 생성
def savePathFile(data, filename="path.txt"):
    imgPathFile = open("path.txt", 'w')
    for path in data:
        path = path + "\n"
        imgPathFile.write(path)
    imgPathFile.close()

def getPathFile(text1, text2, text3, text4, filename="path.txt"):
    if os.path.isfile(filename):
        savePath = open(filename, 'r', encoding='UTF8')
        for i, path in enumerate(savePath.readlines()):
            path = path.strip()
            if i == 0:
                text1.insert("1.0", path)
                imgPathList[i] = path
            if i == 1:
                text2.insert("1.0", path)
                imgPathList[i] = path
            if i == 2:
                text3.insert("1.0", path)
                imgPathList[i] = path
            if i == 3:
                text4.insert("1.0", path)
                imgPathList[i] = path

# returns is value is None or not
def isEmpty(value):
    return value == None

def onclose(root):
    global opened
    opened = False
    root.destroy()

# 이미지 불러오기
def getImg(btn):
    path = askopenfilename(
        title="파일 선택",
        filetypes =(
            ("Image files (*.png, *jpg)", ("*.png", "*.jpg")),
            ("all files (*.*)","*.*")
        )
    )

    if isEmpty(imgPath11Entry) != True and btn == "btn11 clicked":
        imgPath11Entry.delete("1.0", END)
        imgPath11Entry.insert("1.0", "")
    if isEmpty(imgPath12Entry) != True and btn == "btn12 clicked":
        imgPath12Entry.delete("1.0", END)
        imgPath12Entry.insert("1.0", "")
    if isEmpty(imgPath13Entry) != True and btn == "btn13 clicked":
        imgPath13Entry.delete("1.0", END)
        imgPath13Entry.insert("1.0", "")
    if isEmpty(imgPath14Entry) != True and btn == "btn14 clicked":
        imgPath14Entry.delete("1.0", END)
        imgPath14Entry.insert("1.0", "")

    if path != '':
        print("user chose", path)
        if btn == "btn11 clicked":
            imgPath11Entry.insert("1.0", path)
            # if path not in imgPathList:
            #     imgPathList.append(path)
            imgPathList[0] = path

        elif btn == "btn12 clicked":
            imgPath12Entry.insert("1.0", path)
            # if path not in imgPathList:
            #     imgPathList.append(path)
            imgPathList[1] = path

        elif btn == "btn13 clicked":
            imgPath13Entry.insert("1.0", path)
            # if path not in imgPathList:
            #     imgPathList.append(path)
            imgPathList[2] = path

        elif btn == "btn14 clicked":
            imgPath14Entry.insert("1.0", path)
            # if path not in imgPathList:
            #     imgPathList.append(path)
            imgPathList[3] = path
        
    else:
        print("Image Not Selected")

# 로그 파일 불러오기
def getLog():
    path = askopenfilename(
        title="파일 선택",
        filetypes =(
            ("Log files (*.log, *txt)", ("*.log", "*.txt")),
            ("all files (*.*)","*.*")
        )
    )

    if isEmpty(logPathEntry) != True:
        logPathEntry.delete("1.0", END)
        logPathEntry.insert("1.0", "")

    if path != '':
        print("user chose", path)
        logPathEntry.insert("1.0", path)
    else:
        print("Image Not Selected")

setTimeF = False
setTimeT = False
def isTimeSet():
    global setTimeF
    global setTimeT
    tF = playFromVal.get()
    tT = playToVal.get()

    # 둘다 설정 안했을 때 -> 처음부터 시작해서 끝까지
    if tF == "00:00:00" and tT == "23:59:59":
        setTimeF = False
        setTimeT = False

    # 시작시간 설정은 안하고 종료시간만 설정했을 때 -> 처음부터 시작해서 설정한 시간까지
    elif tF == "00:00:00" and tT != "23:59:59":
        setTimeF = False
        setTimeT = True
    
    # 종료시간 설정은 안하고 시작시간만 설정했을 때 -> 설정한 시간부터 시작해서 끝까지
    elif tF != "00:00:00" and tT == "23:59:59":
        setTimeF = True
        setTimeT = False
    
    # 둘다 설정했을 때 -> 설정한 시간부터 시작해서 설정한 시간까지
    elif tF != "00:00:00" and tT != "23:59:59":
        setTimeF = True
        setTimeT = True

opened = False
imgWin = None
img11path = None
img12path = None
img13path = None
img14path = None
logFile = None
player11 = None
player12 = None
player13 = None
player14 = None
log_idx = 0
logfilesize = 0

def playImg(btn):
    global player11, player12, player13, player14
    global opened
    
    global setTimeF
    global setTimeT

    global imgWin
    global img11path
    global img12path
    global img13path
    global img14path
    global logFile
    global log_idx
    global logfilesize

    tF = None
    tT = None
    timeF = None
    timeT = None
    restart = False

    log_idx = getIdx()
    isTimeSet()

    if not opened:
        imgWin = Toplevel()
        imgWin.title("박스 표시")
        opened = True
        imgWin.protocol('WM_DELETE_WINDOW', lambda: onclose(imgWin))
    else:
        restart = True

    if setTimeF == False and setTimeT == True:
        tF = "00:00:00"
        tT = playToVal.get()

    elif setTimeF == True and setTimeT == False:
        tF = playFromVal.get()
        tT = "23:59:59"

    elif setTimeF == True and setTimeT == True:
        tF = playFromVal.get()
        tT = playToVal.get()

    else:
        tF = "00:00:00"
        tT = "23:59:59"

    timeF = datetime.strptime(tF, "%H:%M:%S").time()
    timeT = datetime.strptime(tT, "%H:%M:%S").time()

    if btn == "btn play":
        savePathFile(imgPathList)
        
        img11path = imgPath11Entry.get("1.0", "end-1c")
        img12path = imgPath12Entry.get("1.0", "end-1c")
        img13path = imgPath13Entry.get("1.0", "end-1c")
        img14path = imgPath14Entry.get("1.0", "end-1c")
        logFile = logPathEntry.get("1.0", "end-1c")

        speed = float(playSpeedVal.get())
        logfilesize = len(readLog(logFile))

        # 종료가 아닐 때
        if getFinish() == False:
            # 정지가 아닐 때 이미지 새로 생성 금지
            if getPause() == False:
                player11 = ImagePlayer(imgWin, img11path, 11, 0)
                player12 = ImagePlayer(imgWin, img12path, 12, 0)
                player13 = ImagePlayer(imgWin, img13path, 13, 0)
                player14 = ImagePlayer(imgWin, img14path, 14, 0)
            drawBox(imgWin, player11, player12, player13, player14, logFile, timeF, timeT, log_idx, speed)
        # 종료 후 다시 시작할 때
        else:
            setFinish(False)
            setPause(False)
            log_idx = initIdx()
            showExcept.set(0)
            if not restart:
                player11 = ImagePlayer(imgWin, img11path, 11, 0)
                player12 = ImagePlayer(imgWin, img12path, 12, 0)
                player13 = ImagePlayer(imgWin, img13path, 13, 0)
                player14 = ImagePlayer(imgWin, img14path, 14, 0)
            drawBox(imgWin, player11, player12, player13, player14, logFile, timeF, timeT, log_idx, speed)

    # 일시정지, log_idx 유지
    elif btn == "btn pause":
        setFinish(False)
        setPause(True)
        print("Paused")

    # log_idx -= 1
    elif btn == "btn back":
        print("Back")
        if log_idx - 1 < 0:
            messagebox.showwarning(title="Beginning of Log File", message="BEGINNING OF LOG FILE: 로그의 처음입니다.")
        else:
            prevBox(imgWin, player11, player12, player13, player14, logFile, timeF, timeT, log_idx)

    # log_idx += 1
    elif btn == "btn next":
        print("Next")
        if log_idx + 1 >= logfilesize:
            messagebox.showwarning(title="End of Log File", message="END OF LOG FILE: 로그의 끝입니다.")
        else:
            nextBox(imgWin, player11, player12, player13, player14, logFile, timeF, timeT, log_idx)

    # 재생 중단, log_idx를 0으로 재설정
    elif btn == "btn stop":
        print("Stop")
        setFinish(True)
        setPause(False)
        log_idx = initIdx()
        opened = False
        showExcept.set(0)
        imgWin.destroy()

    # 종료 버튼 누름으로 창 닫기
    elif btn == "btn finish":
        print("Finish")
        win.destroy()
    
    imgWin.mainloop()

def getExcept():
    global player11, player12, player13, player14
    global imgWin
    if showExcept.get() == 1:
        print("예외구역 ON")
        print("showExcept = ", showExcept.get())
        setIsExcept(True)
        drawExcept(imgWin, player11, player12, player13, player14, showExcept.get())
    else:
        print("예외구역 OFF")
        print("showExcept = ", showExcept.get())
        setIsExcept(False)
        drawExcept(imgWin, player11, player12, player13, player14, showExcept.get())

if __name__ == "__main__":

    ''' 11번 이미지 '''
    contain0 = Frame(win)
    contain0.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_11 = Label(contain0, text="11 구역 이미지 경로", font=('Arial', 10))
    imgPath_11.pack(side="left", padx=(30, 0))

    imgPath11Entry = Text(contain0, width=70, height=2)
    imgPath11Entry.pack(side="left")
    btn11 = Button(contain0, text="불러오기", width=15, command=lambda btn="btn11 clicked" : getImg(btn)).pack(side="left", padx=10, pady=5)
    
    ''' 12번 이미지 '''
    contain1 = Frame(win)
    contain1.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_12 = Label(contain1, text="12 구역 이미지 경로", font=('Arial', 10))
    imgPath_12.pack(side="left", padx=(30, 0))
    
    imgPath12Entry = Text(contain1, width=70, height=2)
    imgPath12Entry.pack(side="left")
    btn12 = Button(contain1, text="불러오기", width=15, command=lambda btn="btn12 clicked" : getImg(btn)).pack(side="left", padx=10, pady=5)

    ''' 13번 이미지 '''
    contain2 = Frame(win)
    contain2.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_13 = Label(contain2, text="13 구역 이미지 경로", font=('Arial', 10))
    imgPath_13.pack(side="left", padx=(30, 0))
    
    imgPath13Entry = Text(contain2, width=70, height=2)
    imgPath13Entry.pack(side="left")
    btn13 = Button(contain2, text="불러오기", width=15, command=lambda btn="btn13 clicked" : getImg(btn)).pack(side="left", padx=10, pady=5)

    ''' 14번 이미지 '''
    contain3 = Frame(win)
    contain3.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_14 = Label(contain3, text="14 구역 이미지 경로", font=('Arial', 10))
    imgPath_14.pack(side="left", padx=(30, 0))

    imgPath14Entry = Text(contain3, width=70, height=2)
    imgPath14Entry.pack(side="left")
    btn14 = Button(contain3, text="불러오기", width=15, command=lambda btn="btn14 clicked" : getImg(btn)).pack(side="left", padx=10, pady=5)

    ''' 로그 파일 불러오기 '''
    contain4 = Frame(win)
    contain4.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    logPath = Label(contain4, text="로그파일", font=('Arial', 10))
    logPath.pack(side="left", padx=(30, 65))

    logPathEntry = Text(contain4, width=70, height=2)
    logPathEntry.pack(side="left")
    btnLog = Button(contain4, text="불러오기", width=15, command=getLog).pack(side="left", padx=10, pady=5)

    ''' 예외구역 표시 checkbox '''
    contain5 = Frame(win)
    contain5.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    showExcept = IntVar()
    exceptChkBox = Checkbutton(contain5, text="예외구역 표시", variable=showExcept, command=getExcept).pack(side="left", padx=150, pady=5)
    
    ''' 재생구간 '''
    contain6 = Frame(win)
    contain6.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    playInterval = Label(contain6, text="재생구간", font=('Arial', 10))
    playInterval.pack(side="left", padx=(30, 65))

    playFromVal = StringVar(contain6, value="00:00:00")
    playFromEntry = Entry(contain6, width=20, textvariable = playFromVal)
    playFromEntry.pack(side="left", padx=(0, 3), pady=5)

    playToVal = StringVar(contain6, value="23:59:59")
    playToEntry = Entry(contain6, width=20, textvariable = playToVal)
    playToEntry.pack(side="left", padx=(0, 3), pady=5)

    ''' 재생속도 '''
    contain7 = Frame(win)
    contain7.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    
    playSpeed = Label(contain7, text="재생속도", font=('Arial', 10))
    playSpeed.pack(side="left", padx=(30, 65))
    playSpeedVal = StringVar(contain7, value="10")
    playSpeedEntry = Entry(contain7, width=10, justify=CENTER, textvariable=playSpeedVal)
    playSpeedEntry.pack(side="left", padx=(0, 3), pady=5)
    playSpeedINFO = Label(contain7, text="(1 - 100 사이의 숫자, 숫자가 클수록 느림)", font=('Arial', 10))
    playSpeedINFO.pack(side="left", padx=10)

    ''' 버튼 모음 '''
    contain8  = Frame(win)
    contain8.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)

    btn1 = Button(contain8, text="재생시작", width=15, command=lambda btn="btn play" : playImg(btn)).pack(side="left", padx=(50, 10), pady=5)
    btn2 = Button(contain8, text="일시정지", width=15, command=lambda btn="btn pause" : playImg(btn)).pack(side="left", padx=10, pady=5)
    btn3 = Button(contain8, text="이전", width=15, command=lambda btn="btn back" : playImg(btn)).pack(side="left", padx=10, pady=5)
    btn4 = Button(contain8, text="이후", width=15, command=lambda btn="btn next" : playImg(btn)).pack(side="left", padx=10, pady=5)
    btn5 = Button(contain8, text="중지", width=15, command=lambda btn="btn stop" : playImg(btn)).pack(side="left", padx=10, pady=5)
    btn6 = Button(contain8, text="종료", width=15, command=lambda btn="btn finish" : playImg(btn)).pack(side="left", padx=10, pady=5)

    ''' 저장된 이미지 경로 불러오기 '''
    getPathFile(imgPath11Entry, imgPath12Entry, imgPath13Entry, imgPath14Entry)

    win.mainloop()