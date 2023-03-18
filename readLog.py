import pandas as pd
import json

def readLog(logPath):
    logFile = open(logPath, 'rt', encoding='UTF8')

    analysis = []
    temp = []
    isAnalyze = False

    for i, line in enumerate(logFile):
        if line[33:54] == "=== START ANALIZE ===":
            isAnalyze = True
            if temp != []:
                analysis.append(temp)
                temp = []
            temp.append(line)

        else:
            isAnalyze = False
        
        if isAnalyze == False and i != 0:
            temp.append(line)
    
    return analysis




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



    
    