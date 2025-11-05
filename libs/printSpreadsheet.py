from terminal import *  #¯\_(ツ)_/¯
import os

def printscreen(spreadsheet,originX,originY):
    screenSize = os.get_terminal_size()
    

def makeSquarePrintable(value,collumnSize):
    """
    ya give this the value of a square and your options and it gives you wat to print and how many lines
    """
    valueSTR = str(value)
    finalList = []
    while len(valueSTR) > collumnSize:
        finalList.append(valueSTR[:collumnSize])
        valueSTR = valueSTR[collumnSize:]
    finalList.append(valueSTR)
    return finalList

def makeLinePrintable(valuesList,collumnSize):
    """
    beeg list of all the values is given
    gives a list of lists
    the first list represents all the lines of the terminal that your line will take
    the deeper list repressents all the values in each line
    """
    middleList = []
    for value in range(valuesList):
        middleList.append(makeSquarePrintable(value,collumnSize))
    
    finalList = invertDimentions(middleList)

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
    
    
    
    
    
    