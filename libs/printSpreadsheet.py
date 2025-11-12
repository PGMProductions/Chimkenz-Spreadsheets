from terminal import background  #¯\_(ツ)_/¯
import os
import sys
#j
def printscreen(spreadsheet,originX,originY,collumnSize):
    """
    prints a state of the spreadsheet
    i cant be bothered to make a proper code
    ik this is ugly af, i just hope it'll work and i wont have to come back to it
    """
    screenSize = os.get_terminal_size()
    printList = []                          #list of all the terminal lines it COULD print, might not print them all
    collumnAmmount = screenSize[0]//collumnSize
    usefulLines = []
    for line in range(originY,min(len(spreadsheet),originY+screenSize[1])):
        usefulLines.append(spreadsheet[line][originX:min(originX+screenSize[0],len(spreadsheet[line])-1)])
    
    for line in range(len(usefulLines)):
        for termLine in makeLinePrintable(usefulLines[line],collumnSize,collumnAmmount,line):
            printList.append(termLine)
            
    for i in range(min(len(printList),screenSize[1])):
        print(printList[i])


def makeSquarePrintable(value,collumnSize):
    """
    ya give this the value of a square and your options and it gives you wat to print and how many lines
    """
    valueSTR = str(value)
    finalList = []
    while len(valueSTR) > collumnSize:
        finalList.append(valueSTR[:collumnSize])
        valueSTR = valueSTR[collumnSize:]
        
    finalSTR = " "*(collumnSize-len(valueSTR)) + valueSTR
    finalList.append(finalSTR)
    return finalList

def makeLinePrintable(valuesList,collumnSize,collumnsAmmount,lineNumber):
    """
    beeg list of all the values is given
    gives a list of strings
    each string is a line to print in the terminal
    """
    middleList = []
    for value in range(min(len(valuesList),collumnsAmmount)):
        middleList.append(makeSquarePrintable(valuesList[value],collumnSize))
    
    finalList = []
    middleList = invertDimentions(middleList)
    for line in middleList:
        linestring = ""
        for i in range(len(line)):
            squareColor = 234 + (((lineNumber+i)%2)*6)
            linestring = linestring + generateSetBGColorString(squareColor)
            if line[i] == None:
                linestring = linestring + " "*collumnSize
            else:
                linestring = linestring + line[i]
        finalList.append(linestring)
    return finalList


def generateHeader(originX,collumnAmmount,collumnSize):               #not made yet
    return [background(255," "*collumnSize)] * collumnAmmount


def generateSetBGColorString(ID):
    return f"\x1b[48;5;{ID}m"

    #The table starts with the original 16 colors (0-15).
    #The proceeding 216 colors (16-231) or formed by a 3bpc RGB value offset by 16, packed into a single value.
    #The final 24 colors (232-255) are grayscale starting from a shade slighly lighter than black, ranging up to shade slightly darker than white.



def resetBGColor():
    color = "253"
    sys.stdout.write(f"\x1b[48;5;{color}m")
    sys.stdout.flush()



def invertDimentions(liste):
    """
    give it a 2-dimentional list and it'll invert those dimensions
    """
    finalList = []
    shouldContinue = True
    counter = 0
    while shouldContinue:
        tempList = []
        shouldContinue = False
        for i in range(len(liste)):
            if counter < len(liste[i]):
                tempList.append(liste[i][counter])
                shouldContinue = True
            else:
                tempList.append(None)
            
        finalList.append(tempList)
        counter += 1
    finalList.pop(-1)
    return finalList
    





printscreen([[9.123456789,2,3,4,5,6,6],
             [2,2,2,2,2,2,2],
             [9,8,7,6,6,5,4],
             [9,9,9,912345678901234567890,9,9,9],
             [1,1,1,1,2,2,2],
             [1,2,3,4,5,6,7],
             [0,0,0,0,0,0,0]],0,0,15)


    
    
    
    