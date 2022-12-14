# TODO:
inputFile = open('input2.txt', 'r')

data = inputFile.read().splitlines()

yLines = len(data)
xLines = len(data[0])

# x,y -> isHidden
treeMap = {}

xIndex = 0
for line in data:
    # scan X axis
    xIndex+=1
    treeMap[xIndex] = {} # create new x axis in treemap
    yIndex = 0
    for treeNumber in line:
        # scan Y axis
        yIndex+=1

        isHidden = True

        # scan up
        if xIndex <= 1: # if top border
            isHidden = False
        else: # if not on top border

            print(yIndex, xIndex)
 

        # scan right
        if yIndex >= yLines: # if right border
            isHidden = False
        #else: # if not on right border

        # scan down
        if xIndex >= xLines: # if bottom border
            isHidden = False
        #else: # if not on bottom border

        # scan left
        if yIndex <= 1: # if on left border
            isHidden = False
        #else: # if not on left border


        #if isHidden:
            #print('current tree: ' + treeNumber) # DEBUG!!!!

        treeMap[xIndex][yIndex] = isHidden # add current tree to treemap

        if(yIndex <= yLines): # end of y axis
            yLines == 0
 
    if(xIndex <= xLines): # end of x axis
            yLines == 0

print(treeMap)