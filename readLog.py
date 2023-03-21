import pandas as pd
from datetime import datetime

'''
    analysis 리스트안에는 분석 1회에 대한 정보가 들어있음
    한 개의 아이템은 START ANALYZE로 시작함, 아이템별로 length가 다름
'''
def readLog(logPath):
    logFile = open(logPath, 'rt', encoding='UTF8')

    analysis = []
    temp = []
    isAnalyze = False

    for i, line in enumerate(logFile):
        if line[33:54] == "=== START ANALIZE ===":
            isAnalyze = True
            # 1회 분석을 기준으로 리스트 업데이트
            if temp != []:
                analysis.append(temp)
                temp = []
            # temp.append(line)

        else:
            isAnalyze = False

        info = line[33:].split(", ")
        
        if isAnalyze == False and i != 0:
            # DEBUG 메시지 제외
            if line[25:32] == "[DEBUG]":
                pass
            if info[0].startswith("Detect object") or info[0].startswith("MQTT"):
                temp.append(line)
            # 이벤트 발생 메시지 제외

    return analysis


# TODO
# 1회 분석에서 시간 정보 가져오기
def getTime(analyze):

    timeInfo = analyze[1:24]

    # ymd = [year, month, day] 
    ymd = timeInfo[:10].split("-")

    # hms = "hour:min:sec"
    hms = timeInfo[12:].split(",")[0]
    analyzeTime = datetime.strptime(hms, "%H:%M:%S").time()

    return ymd, analyzeTime

# 1회 분석에서 예외구역인지 아닌지 판단
def isValid(analyze):
    allInfo = analyze[33:].split(", ")
    if "VALID" in allInfo[0]:
        return True
    elif "EX" in allInfo[0]:
        return False

# 1회 분석에서 장비 번호 가져오기
def getDeviceID(analyze):
    allInfo = analyze[33:].split(", ")
    dID = allInfo[0][len(allInfo[0]) - 2:]
    return dID

# 1회 분석에서 감지 객체 가져오기
def getObject(analyze):
    allInfo = analyze[33:].split(", ")
    obj = allInfo[1]
    return obj

# 1회 분석에서 박스 정보(x, y, w, h) 가져오기
def getBox(analyze):
    allInfo = analyze[33:].split(", ")
    boxInfo = allInfo[2:6]
    x, y, w, h = [int(e) for e in boxInfo]
    return x, y, w, h

'''
    readLog.py TEST
    Analysis 리스트에 잘 들어가는 거 확인 O
    다른 function들 작동 확인 O
'''
# import json
# path = "C:/Users/USER/Desktop/Programs/Corners_programs/pythontools/대상WL 로그재현 Tool/log/DetectManager20230317.log"
# analysis = readLog(path)

# for item in analysis:
#     for i in range(len(item)):
#         iDate, iTime = getTime(item[i])
#         print("Analyze Date: ", iDate)
#         print("Analyze Time: ", iTime)
#         print("Is Valid: ", isValid(item[i]))
#         print("Device ID: ", getDeviceID(item[i]))
#         print("Detect Object: ", getObject(item[i]))
#         print("X, Y, W, H: ", getBox(item[i]))
#         print("\n")

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