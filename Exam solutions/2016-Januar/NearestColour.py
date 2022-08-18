import numpy as np
def nearestColor(r,g,b):
    table = np.array([
        ["White",100,100,100],
        ['Grey',50,50,50],
        ['Black',0,0,0],
        ['Red',100,0,0],
        ['Maroon',50,0,0],
        ["Yellow",100,100,0],
        ["Olive",50,50,0],
        ['Lime',0,100,0],
        ['Green',0,50,0],
        ['Aqua',0,100,100],
        ["Teal",0,50,50],
        ["Blue",0,0,100],
        ['Navy',0,0,50],
        ['Fuchsia',100,0,100],
        ['Purple',50,0,50],
    ])
    minD = None
    colorName = ''
    for color in table:
        colName = color[0]
        colR = int(color[1])
        colG = int(color[2])
        colB = int(color[3])
        D = max(abs(r-colR),abs(g-colG),abs(b-colB))
        if minD is None or D < minD:
            minD = D
            colorName = colName
    return colorName

print(nearestColor(75,0,0))
