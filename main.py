import cv2
import numpy as np
import psycopg2
import os
import json

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
win.geometry("900x600")


def sample():
    print("cbal")


if __name__ == "__main__":

    ''' 11번 이미지 '''
    contain0 = Frame(win)
    contain0.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_11 = Label(contain0, text="11 구역 이미지 경로", font=('Arial', 10))
    imgPath_11.pack(side="left", padx=(30, 0))

    imgPath11Entry = Text(contain0, width=49, height=2)
    imgPath11Entry.pack(side="left")
    Button(contain0, text="불러오기", width=15, command=sample).pack(side="left", padx=10, pady=5)
    
    ''' 12번 이미지 '''
    contain1 = Frame(win)
    contain1.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_12 = Label(contain1, text="12 구역 이미지 경로", font=('Arial', 10))
    imgPath_12.pack(side="left", padx=(30, 0))
    
    imgPath12Entry = Text(contain1, width=49, height=2)
    imgPath12Entry.pack(side="left")
    Button(contain1, text="불러오기", width=15, command=sample).pack(side="left", padx=10, pady=5)

    ''' 13번 이미지 '''
    contain2 = Frame(win)
    contain2.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_13 = Label(contain2, text="13 구역 이미지 경로", font=('Arial', 10))
    imgPath_13.pack(side="left", padx=(30, 0))
    
    imgPath13Entry = Text(contain2, width=49, height=2)
    imgPath13Entry.pack(side="left")
    Button(contain2, text="불러오기", width=15, command=sample).pack(side="left", padx=10, pady=5)

    ''' 14번 이미지 '''
    contain3 = Frame(win)
    contain3.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    imgPath_14 = Label(contain3, text="14 구역 이미지 경로", font=('Arial', 10))
    imgPath_14.pack(side="left", padx=(30, 0))

    imgPath14Entry = Text(contain3, width=49, height=2)
    imgPath14Entry.pack(side="left")
    Button(contain3, text="불러오기", width=15, command=sample).pack(side="left", padx=10, pady=5)

    ''' 로그 파일 불러오기 '''
    contain4 = Frame(win)
    contain4.pack(side="top", anchor=NW, expand=True, fill=BOTH, padx=10)
    logPath = Label(contain4, text="로그파일", font=('Arial', 10))
    logPath.pack(side="left", padx=(30, 65))

    logPathEntry = Text(contain4, width=49, height=2)
    logPathEntry.pack(side="left")
    Button(contain4, text="불러오기", width=15, command=sample).pack(side="left", padx=10, pady=5)

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

    # cIDvalue = Label(contain5, text="pos", font=('Arial', 10))
    # cIDvalue.pack(side="left", padx=(93, 12), pady=5)

    playFrom = Label(contain6, text="From", font=('Arial', 10))
    playFrom.pack(side="left", padx=(93, 12), pady=5)

    playTo = Label(contain6, text="To", font=('Arial', 10))
    playTo.pack(side="left", padx=(93, 12), pady=5)

    win.mainloop()