import pandas as pd
import json

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
            temp.append(line)

        else:
            isAnalyze = False
        
        if isAnalyze == False and i != 0:
            # DEBUG 메시지는 뺀다
            if line[25:32] == "[DEBUG]":
                pass
            else:
                temp.append(line)
    
    return analysis


# TODO
# 분석에서 시간 정보 가져오기
def getTime(analysis):
    return

# 분석에서 장비 번호 가져오기
def getDeviceID(analysis):
    dID = 0
    return dID

# 분석에서 박스 정보(x, y, w, h) 가져오기
def getBox(analysis):
    x, y, w, h = 0, 0, 0, 0
    return (x, y, w, h)





'''
    readLog.py TEST
    Analysis 리스트에 잘 들어가는 거 확인했음
'''
# path = "D:/Corners/대상WL 로그재현 Tool/log/DetectManager20230317.log"
# analysis = readLog(path)
# newJson = {"Analysis Test":[]}
# json_obj = json.dumps(newJson, indent=4)
# with open("analysis_test.json", 'w') as outfile:
#     outfile.write(json_obj)

# with open("analysis_test.json", 'r+') as file:
#     file_data = json.load(file)
#     for item in analysis:
#         file_data["Analysis Test"].append(item)
    
#     file.seek(0)
#     json.dump(file_data, file, indent=4)



    
    