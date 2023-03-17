import cv2
import numpy as np
import pandas as pd
import os
import json

# import from local py
from readLog import *

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
win.geometry("900x300")

'''
TODO
* 로그파일 불러와서 읽기
* 재생구간 콤보박스 정보 불러와서 로그에서 그 구간의 데이터만 읽기
* 하단 버튼 기능 전부 구현
* 이미지 경로 tkinter 윈도우에 4개 연속으로 띄워서 박스 그리기
'''


def sample():
    print("cbal")

def sample2():
    p = logPathEntry.get("1.0", "end-1c")
    readLog(p)

def getImg(btn):
    path = askopenfilename(
        title="파일 선택",
        filetypes =(
            ("Image files (*.png, *jpg)", ("*.png", "*.jpg")),
            ("all files (*.*)","*.*")
        )
    )

    if path != '':
        print("user chose", path)
        if btn == "btn11 clicked":
            imgPath11Entry.insert("1.0", path)
        elif btn == "btn12 clicked":
            imgPath12Entry.insert("1.0", path)
        elif btn == "btn13 clicked":
            imgPath13Entry.insert("1.0", path)
        elif btn == "btn14 clicked":
            imgPath14Entry.insert("1.0", path)

    else:
        print("Image Not Selected")

def getLog():
    path = askopenfilename(
        title="파일 선택",
        filetypes =(
            ("Log files (*.log)", ("*.log")),
            ("all files (*.*)","*.*")
        )
    )

    if path != '':
        print("user chose", path)
        logPathEntry.insert("1.0", path)

    else:
        print("Image Not Selected")

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
    exceptChkBox = Checkbutton(contain5, text="예외구역 표시", variable=showExcept).pack(side="left", padx=150, pady=5)
    
    ''' 재생구간 '''
    contain6 = Frame(win)
    contain6.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    playInterval = Label(contain6, text="재생구간", font=('Arial', 10))
    playInterval.pack(side="left", padx=(30, 65))

    timeList = [
        "07:00", "07:30",
        "08:00", "08:30",
        "09:00", "09:30",
        "10:00", "10:30",
        "11:00", "11:30",
        "12:00","12:30",
        "13:00", "13:30",
        "14:00", "14:30", 
        "15:00", "15:30",
        "16:00", "16:30",
        "17:00", "17:30",
        "18:00", "18:30",
        "19:00", "19:30",
        "20:00", "20:30"]

    playFrom = ttk.Combobox(contain6, width=15, height=5, values=timeList)
    playFrom.set("시작시간")
    playFrom.pack(side="left", padx=(0, 3), pady=5)

    playTo = ttk.Combobox(contain6, width=15, height=5, values=timeList)
    playTo.set("종료시간")
    playTo.pack(side="left", padx=(0, 3), pady=5)

    ''' 버튼 모음 '''
    contain7  = Frame(win)
    contain7.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)

    btn1 = Button(contain7, text="재생시작", width=15, command=sample2).pack(side="left", padx=(50, 10), pady=5)
    btn2 = Button(contain7, text="일시정지", width=15, command=sample).pack(side="left", padx=10, pady=5)
    btn3 = Button(contain7, text="이전", width=15, command=sample).pack(side="left", padx=10, pady=5)
    btn4 = Button(contain7, text="이후", width=15, command=sample).pack(side="left", padx=10, pady=5)
    btn5 = Button(contain7, text="중지", width=15, command=sample).pack(side="left", padx=10, pady=5)
    btn6 = Button(contain7, text="종료", width=15, command=sample).pack(side="left", padx=10, pady=5)

    win.mainloop()