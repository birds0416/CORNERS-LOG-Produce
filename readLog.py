import pandas as pd

def readLog(logPath):
    logFile = open(logPath, 'rt', encoding='UTF8')

    analysis = []

    for i, line in enumerate(logFile):

        temp = []
        # time = line[1:24]
        # allInfo = line[33:].split(', ')
        # print(allInfo)
        if line[33:54] != "=== START ANALIZE ===" and i != 0:
            temp.append(line)




path = "D:/Corners/대상WL 로그재현 Tool/log/DetectManager20230317.log"
readLog(path)