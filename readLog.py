import pandas as pd
from datetime import datetime
from tkinter import messagebox
import re

'''
    analysis 리스트안에는 분석 1회에 대한 정보가 들어있음
    한 개의 아이템은 START ANALYZE로 시작함, 아이템별로 length가 다름
'''

def getFileSize(logPath):
    size = 0
    analysis = []
    temp = []
    isAnalyze = False
    try:
        logFile = open(logPath, 'rt', encoding='cp949')
        for idx, line in enumerate(logFile):
            if line[33:54] == "=== START ANALIZE ===":
                isAnalyze = True
                # 1회 분석을 기준으로 리스트 업데이트
                if temp != []:
                    size += 1
                    analysis.append(temp)
                    temp = []
            
            else:
                isAnalyze = False
            
            info = line[33:].split(",")
            new_info = []
            for i in info:
                new_info.append(i.strip())
            
            if isAnalyze == False and idx != 0:
                # DEBUG 메시지 제외
                if line[25:32] == "[DEBUG]":
                    pass
                if new_info[0].startswith("Detect object VALID") or new_info[0].startswith("Detect object EX"):
                    temp.append(line)
                # 이벤트 발생 메시지 제외

        analysis.append(temp)
        temp = []
            
    except UnicodeDecodeError:
        try:
            logFile = open(logPath, 'rt', encoding='UTF8')
            for idx, line in enumerate(logFile):
                if line[33:54] == "=== START ANALIZE ===":
                    isAnalyze = True
                    # 1회 분석을 기준으로 리스트 업데이트
                    if temp != []:
                        size += 1
                        analysis.append(temp)
                        temp = []
                
                else:
                    isAnalyze = False
                
                info = line[33:].split(",")
                new_info = []
                for i in info:
                    new_info.append(i.strip())
                
                if isAnalyze == False and idx != 0:
                    # DEBUG 메시지 제외
                    if line[25:32] == "[DEBUG]":
                        pass
                    if new_info[0].startswith("Detect object VALID") or new_info[0].startswith("Detect object EX"):
                        temp.append(line)
                    # 이벤트 발생 메시지 제외

            analysis.append(temp)
            temp = []

        except UnicodeDecodeError:
            # If the file is not encoded in utf-8 either, handle the error
            messagebox.showerror(title="File Format Not Supported", message=f'Error: {logPath} 가 cp949 or utf-8 형식으로 인코딩되어야 합니다.')
            print(f'Error: {logPath} is not encoded in cp949 or utf-8.')

    return size

def readLog(logPath):
    all_lines = []
    evt_lines = []
    try:
        logFile = open(logPath, 'rt', encoding='cp949')
        all_lines = logFile.readlines()
    except UnicodeDecodeError:
        try:
            logFile = open(logPath, 'rt', encoding='UTF8')
            all_lines = logFile.readlines()
        except UnicodeDecodeError:
            messagebox.showerror(title="File Format Not Supported", message=f'Error: {logPath} 가 cp949 or utf-8 형식으로 인코딩되어야 합니다.')
            print(f'Error: {logPath} is not encoded in cp949 or utf-8.')
    
    pattern = r"이벤트 발생 \[(\d+)\]"
    for idx, line in enumerate(all_lines):
        if line[33:43] == "### 이벤트 발생":
            match = re.search(pattern, line)
            if match:
                evt_num = int(match.group(1))
                evt_lines.append((idx, evt_num))
    return all_lines, evt_lines

def getPreviousLines(all_lines, evt_idx, lines_before=200):
    start_idx = max(evt_idx - lines_before, 0)
    while start_idx > 0 and "=== START ANALIZE ===" not in all_lines[start_idx]:
        start_idx -= 1
    return all_lines[start_idx:evt_idx + 1]

def getAnalysis(lines):
    temp = []
    analysis = []
    isAnalyze = False
    for idx, line in enumerate(lines):
        if line[33:54] == "=== START ANALIZE ===":
            isAnalyze = True
            # 1회 분석을 기준으로 리스트 업데이트
            if temp != []:
                analysis.append(temp)
                temp = []
        else:
            isAnalyze = False
        
        info = line[33:].split(",")
        new_info = []
        for i in info:
            new_info.append(i.strip())
        
        if isAnalyze == False and idx != 0:
            # DEBUG 메시지 제외
            if line[25:32] == "[DEBUG]":
                pass
            if new_info[0].startswith("Detect object VALID") or new_info[0].startswith("Detect object EX"):
                temp.append(line)
            # 이벤트 발생 메시지 제외

    analysis.append(temp)
    temp = []
    return analysis

# TODO
# 1회 분석에서 시간 정보 가져오기
def getTime(analyze):
    timeInfo = []
    for data in analyze:
        timeInfo.append(data[1:24])

    # ymd = [year, month, day] 
    ymd = []
    # hms = "hour:min:sec"
    analyzeTime = []
    for time in timeInfo:
        ymd.append(time[:10].split("-"))
        hms = time[11:].split(",")[0]
        analyzeTime.append(datetime.strptime(hms, "%H:%M:%S").time())
    
    return ymd, analyzeTime

# 1회 분석에서 예외구역인지 아닌지 판단
def isValid(analyze):
    info = []
    for data in analyze:
        temp = data[33:].split(",")
        each_info = []
        for t in temp:
            new_t = t.strip()
            each_info.append(new_t)
        info.append(each_info)
    
    valid = []
    for i in info:
        temp = i[0].split('=')[0].strip().replace("Detect object ", "")
        if "VALID" in temp:
            valid.append("VALID")
        elif "EX" in temp:
            valid.append("EX")
    
    return valid
    
# 1회 분석에서 장비 번호 가져오기
def getDeviceID(analyze):

    info = []
    for data in analyze:
        temp = data[33:].split(",")
        each_info = []
        for t in temp:
            new_t = t.strip()
            each_info.append(new_t)
        info.append(each_info)

    dID = []
    for d in info:
        temp = d[0].split('=')[1].strip()
        dID.append(temp)

    return dID

# 1회 분석에서 감지 객체 가져오기
def getObject(analyze):
    info = []
    for data in analyze:
        temp = data[33:].split(",")
        each_info = []
        for t in temp:
            new_t = t.strip()
            each_info.append(new_t)
        info.append(each_info)
    
    obj = []
    for o in info:
        obj.append(o[1])

    return obj

# 1회 분석에서 박스 정보(x, y, w, h) 가져오기
def getBox(analyze):
    info = []
    for data in analyze:
        temp = data[33:].split(",")
        each_info = []
        for t in temp:
            new_t = t.strip()
            each_info.append(new_t)
        info.append(each_info)

    boxInfo = []
    for b in info:
        x, y, w, h = [int(e) for e in b[2:6]]
        boxInfo.append([x, y, w, h])

    return boxInfo

'''
    readLog.py TEST
    Analysis 리스트에 잘 들어가는 거 확인 O
    다른 function들 작동 확인 O
'''
# path = "./log/9290.txt"
# print(getFileSize(path))

# import json
# path = "./log/DetectManager20230328.log"
# path = "./log/DetectManager20231207.log"
# all_lines, evt_lines = readLog(path)

# evt_num_to_find = 11666
# analysis = []
# for idx, evt_num in evt_lines:
#     if evt_num == evt_num_to_find:
#         lines = getPreviousLines(all_lines, idx, 200)
#         # print("Lines around event: ", evt_num_to_find)
#         analysis = getAnalysis(lines)

# for idx, item in enumerate(analysis):
#     # print(item)
# #     # for i in item:
# #     #     print(i)
#     iDate, iTime = getTime(item)
#     print("Analyze Date: ", iDate)
#     print("Analyze Time: ", iTime)
#     print("Is Valid: ", isValid(item))
#     print("Device ID: ", getDeviceID(item))
#     print("Detect Object: ", getObject(item))
#     print("X, Y, W, H: ", getBox(item))
#     # print("evtNum: 12700? {}".format(findEvt(item, 12700)))
#     print("\n")

# newJson = {"Analysis Test":[]}
# json_obj = json.dumps(newJson, indent=4)
# with open("analysis_test.json", 'w') as outfile:
#     outfile.write(json_obj)

# with open("analysis_test.json", 'r+', encoding='utf-8') as file:
#     file_data = json.load(file)
#     for item in analysis:
#         file_data["Analysis Test"].append(item)
    
#     file.seek(0)
#     json.dump(file_data, file, indent=4, ensure_ascii=False)