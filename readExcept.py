import json

jsonPath = "./except_region/config.json"
with open(jsonPath, 'r') as rf:
    region = json.load(rf)

def getRegion(deviceID, f=region):
    coord = ""
    for item in f:
        if deviceID in item:
            coord = f[item]
    return coord

def pnt2draw(coord):
    shapes = []
    tempData = []
    if ":" in coord:
        tempData = coord.split(":")
    else:
        tempData = [coord]
    
    for tmp in tempData:
        each = tmp.split(", ")
        pnts = []
        for e in each:
            X = int(e.split(',')[0])
            Y = int(e.split(',')[1])
            pnts.append([X, Y])
        shapes.append(pnts)
    
    return shapes