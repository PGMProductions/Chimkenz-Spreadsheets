import os
import sys



#This code is ugly but it works so it's okay

SKIPCOLLUMNAMMOUNT = 3
SELECTEDTEXTCOLOR = 88
SELECTEEDSQUARECOLOR = 253

def printScreen(spreadsheet,originX,originY,collumnSize,cursorX,cursorY,skipLineAmmount):                      #big main fuc, should be the only one used by any exterior program
    """
    !!! WARNING !!! only ever input a rectangle  (actually, it might be fine not to, but I never tested it so just be normal)

    prints a state of the spreadsheet
    i cant be bothered to make a proper code
    ik this is ugly af, i just hope it'll work and i wont have to come back to it
    """
    spreadsheetCollumnAmmount = len(spreadsheet[0][originX:])
    for line in spreadsheet:
        assert len(line[originX:]) == spreadsheetCollumnAmmount      #checks if it is a rectangle aka if all the lines are of the same lenght
    assert(collumnSize > 5,"You are not allowed to use less than 5 ad the collumn size\nif you belive this is an error, feel free to disable that by commenting the line 23 in libs/printSpreadsheet")


    screenSize = os.get_terminal_size()
    printList = []                          #list of all the terminal lines it COULD print, might not print them all
    maxCollumnAmmount = (screenSize[0]-SKIPCOLLUMNAMMOUNT)//collumnSize
    usefulLines = []

    for line in range(originY,min(len(spreadsheet),originY+(screenSize[0]-skipLineAmmount))):     #creates a list of only the lines that might be useful
        usefulLines.append(spreadsheet[line][originX:min(originX+screenSize[0],len(spreadsheet[line])-1)])

    if len(usefulLines) < screenSize[1] - skipLineAmmount:
        for _ in range(screenSize[1] - skipLineAmmount - len(usefulLines)):
            usefulLines.append([None for _ in range(spreadsheetCollumnAmmount)])                      #adds empty squares

    for line in range(len(usefulLines)):                                                          #makes that list into a list of strings, one per line
        isFirstTermLine = True
        for termLine in makeLinePrintable(usefulLines[line],collumnSize,maxCollumnAmmount,line+originY,cursorX,(cursorY == line+originY),originX):
            if isFirstTermLine:
                isFirstTermLine = False
                printList.append(generateLineHead(line+originY) + termLine)
            else:
                printList.append(generateLineHead(None) + termLine)                               #generateLineHead of none just adds the 3 spaces



    print("\n" + generateHeader(originX,maxCollumnAmmount,collumnSize))       #the \n is a bandaid fix cuz ninput is weird
    for i in range(min(len(printList),screenSize[1]-skipLineAmmount)):
        print(printList[i])

    print(generateSetBGColorString(0) + generateSetTextColorString(15)) 


def makeSquarePrintable(value,collumnSize):                                                    #fairily complicated but tested, works fine

    """ya give this the value of a square and your options and it gives you wat to print and how many lines"""

    if value == None:
        valueSTR = ""
    elif type(value) == str:
        valueSTR = f"'{value}'"
    else:
        valueSTR = str(value)


    finalList = []
    while len(valueSTR) > collumnSize:
        finalList.append(valueSTR[:collumnSize])
        valueSTR = valueSTR[collumnSize:]
        
    finalSTR = " "*(collumnSize-len(valueSTR)) + valueSTR
    finalList.append(finalSTR)
    return finalList


def makeLinePrintable(valuesList,collumnSize,collumnAmmount,lineNumber,cursorX,isCursorLine,originX):  #fairily complicated but tested, works fine
    """                                                     # ^ only here to determine the color ^
    beeg list of all the values is given
    gives a list of strings
    each string is a line to print in the terminal
    """
    middleList = []
    for value in range(min(len(valuesList),collumnAmmount)):
        middleList.append(makeSquarePrintable(valuesList[value],collumnSize))

    if len(middleList) < collumnAmmount:
        for _ in range(collumnAmmount-len(middleList)):
            middleList.append("")
    
    finalList = []
    middleList = invertDimentions(middleList)
    for line in middleList:
        linestring = ""
        for i in range(len(line)):
            squareColor = 234 + (((lineNumber+i+originX)%2)*6)
            textColor = 249 + (((lineNumber+i+originX)%2)*5)
            if isCursorLine and (i+originX == cursorX):
                squareColor = SELECTEEDSQUARECOLOR
                textColor = SELECTEDTEXTCOLOR
            linestring = linestring + generateSetBGColorString(squareColor) + generateSetTextColorString(textColor)
            if line[i] == None:
                linestring = linestring + " "*collumnSize
            else:
                linestring = linestring + line[i]
        finalList.append(linestring)
    return finalList


def generateHeader(originX,collumnAmmount,collumnSize):                                        #its basically nothing

    headString = "   "                                     #3 spaces because its the line header size
    for i in range(collumnAmmount):
        headString = headString + " " + nameCollumn(i+originX)
        headString = headString + (" " * (((i+1)*collumnSize) - len(headString) + 3))     #this line adds as many spaces as neeeded to complete the square

    return generateSetBGColorString(254) + generateSetTextColorString(0) + headString + generateSetTextColorString(15)


def generateLineHead(line):                                                                    #pretty simple and tested
    if line == None:
        return generateSetBGColorString(254) + "   " + generateSetTextColorString(15) 
    numberStr = str(line)
    numberStr = " " * (3-len(numberStr)) + numberStr
    return generateSetBGColorString(254) + generateSetTextColorString(0) + numberStr + generateSetTextColorString(15) 

def nameCollumn(collumn):                                                                      #completely stupid but stupidely simple
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA" , "AB" , "AC" , "AD" , "AE" , "AF" , "AG" , "AH" , "AI" , "AJ" , "AK" , "AL" , "AM" , "AN" , "AO" , "AP" , "AQ" , "AR" , "AS" , "AT" , "AU" , "AV" , "AW" , "AX" , "AY" , "AZ" , "BA" , "BB" , "BC" , "BD" , "BE" , "BF" , "BG" , "BH" , "BI" , "BJ" , "BK" , "BL" , "BM" , "BN" , "BO" , "BP" , "BQ" , "BR" , "BS" , "BT" , "BU" , "BV" , "BW" , "BX" , "BY" , "BZ" , "CA" , "CB" , "CC" , "CD" , "CE" , "CF" , "CG" , "CH" , "CI" , "CJ" , "CK" , "CL" , "CM" , "CN" , "CO" , "CP" , "CQ" , "CR" , "CS" , "CT" , "CU" , "CV" , "CW" , "CX" , "CY" , "CZ" , "DA" , "DB" , "DC" , "DD" , "DE" , "DF" , "DG" , "DH" , "DI" , "DJ" , "DK" , "DL" , "DM" , "DN" , "DO" , "DP" , "DQ" , "DR" , "DS" , "DT" , "DU" , "DV" , "DW" , "DX" , "DY" , "DZ" , "EA" , "EB" , "EC" , "ED" , "EE" , "EF" , "EG" , "EH" , "EI" , "EJ" , "EK" , "EL" , "EM" , "EN" , "EO" , "EP" , "EQ" , "ER" , "ES" , "ET" , "EU" , "EV" , "EW" , "EX" , "EY" , "EZ" , "FA" , "FB" , "FC" , "FD" , "FE" , "FF" , "FG" , "FH" , "FI" , "FJ" , "FK" , "FL" , "FM" , "FN" , "FO" , "FP" , "FQ" , "FR" , "FS" , "FT" , "FU" , "FV" , "FW" , "FX" , "FY" , "FZ" , "GA" , "GB" , "GC" , "GD" , "GE" , "GF" , "GG" , "GH" , "GI" , "GJ" , "GK" , "GL" , "GM" , "GN" , "GO" , "GP" , "GQ" , "GR" , "GS" , "GT" , "GU" , "GV" , "GW" , "GX" , "GY" , "GZ" , "HA" , "HB" , "HC" , "HD" , "HE" , "HF" , "HG" , "HH" , "HI" , "HJ" , "HK" , "HL" , "HM" , "HN" , "HO" , "HP" , "HQ" , "HR" , "HS" , "HT" , "HU" , "HV" , "HW" , "HX" , "HY" , "HZ" , "IA" , "IB" , "IC" , "ID" , "IE" , "IF" , "IG" , "IH" , "II" , "IJ" , "IK" , "IL" , "IM" , "IN" , "IO" , "IP" , "IQ" , "IR" , "IS" , "IT" , "IU" , "IV" , "IW" , "IX" , "IY" , "IZ" , "JA" , "JB" , "JC" , "JD" , "JE" , "JF" , "JG" , "JH" , "JI" , "JJ" , "JK" , "JL" , "JM" , "JN" , "JO" , "JP" , "JQ" , "JR" , "JS" , "JT" , "JU" , "JV" , "JW" , "JX" , "JY" , "JZ" , "KA" , "KB" , "KC" , "KD" , "KE" , "KF" , "KG" , "KH" , "KI" , "KJ" , "KK" , "KL" , "KM" , "KN" , "KO" , "KP" , "KQ" , "KR" , "KS" , "KT" , "KU" , "KV" , "KW" , "KX" , "KY" , "KZ" , "LA" , "LB" , "LC" , "LD" , "LE" , "LF" , "LG" , "LH" , "LI" , "LJ" , "LK" , "LL" , "LM" , "LN" , "LO" , "LP" , "LQ" , "LR" , "LS" , "LT" , "LU" , "LV" , "LW" , "LX" , "LY" , "LZ" , "MA" , "MB" , "MC" , "MD" , "ME" , "MF" , "MG" , "MH" , "MI" , "MJ" , "MK" , "ML" , "MM" , "MN" , "MO" , "MP" , "MQ" , "MR" , "MS" , "MT" , "MU" , "MV" , "MW" , "MX" , "MY" , "MZ" , "NA" , "NB" , "NC" , "ND" , "NE" , "NF" , "NG" , "NH" , "NI" , "NJ" , "NK" , "NL" , "NM" , "NN" , "NO" , "NP" , "NQ" , "NR" , "NS" , "NT" , "NU" , "NV" , "NW" , "NX" , "NY" , "NZ" , "OA" , "OB" , "OC" , "OD" , "OE" , "OF" , "OG" , "OH" , "OI" , "OJ" , "OK" , "OL" , "OM" , "ON" , "OO" , "OP" , "OQ" , "OR" , "OS" , "OT" , "OU" , "OV" , "OW" , "OX" , "OY" , "OZ" , "PA" , "PB" , "PC" , "PD" , "PE" , "PF" , "PG" , "PH" , "PI" , "PJ" , "PK" , "PL" , "PM" , "PN" , "PO" , "PP" , "PQ" , "PR" , "PS" , "PT" , "PU" , "PV" , "PW" , "PX" , "PY" , "PZ" , "QA" , "QB" , "QC" , "QD" , "QE" , "QF" , "QG" , "QH" , "QI" , "QJ" , "QK" , "QL" , "QM" , "QN" , "QO" , "QP" , "QQ" , "QR" , "QS" , "QT" , "QU" , "QV" , "QW" , "QX" , "QY" , "QZ" , "RA" , "RB" , "RC" , "RD" , "RE" , "RF" , "RG" , "RH" , "RI" , "RJ" , "RK" , "RL" , "RM" , "RN" , "RO" , "RP" , "RQ" , "RR" , "RS" , "RT" , "RU" , "RV" , "RW" , "RX" , "RY" , "RZ" , "SA" , "SB" , "SC" , "SD" , "SE" , "SF" , "SG" , "SH" , "SI" , "SJ" , "SK" , "SL" , "SM" , "SN" , "SO" , "SP" , "SQ" , "SR" , "SS" , "ST" , "SU" , "SV" , "SW" , "SX" , "SY" , "SZ" , "TA" , "TB" , "TC" , "TD" , "TE" , "TF" , "TG" , "TH" , "TI" , "TJ" , "TK" , "TL" , "TM" , "TN" , "TO" , "TP" , "TQ" , "TR" , "TS" , "TT" , "TU" , "TV" , "TW" , "TX" , "TY" , "TZ" , "UA" , "UB" , "UC" , "UD" , "UE" , "UF" , "UG" , "UH" , "UI" , "UJ" , "UK" , "UL" , "UM" , "UN" , "UO" , "UP" , "UQ" , "UR" , "US" , "UT" , "UU" , "UV" , "UW" , "UX" , "UY" , "UZ" , "VA" , "VB" , "VC" , "VD" , "VE" , "VF" , "VG" , "VH" , "VI" , "VJ" , "VK" , "VL" , "VM" , "VN" , "VO" , "VP" , "VQ" , "VR" , "VS" , "VT" , "VU" , "VV" , "VW" , "VX" , "VY" , "VZ" , "WA" , "WB" , "WC" , "WD" , "WE" , "WF" , "WG" , "WH" , "WI" , "WJ" , "WK" , "WL" , "WM" , "WN" , "WO" , "WP" , "WQ" , "WR" , "WS" , "WT" , "WU" , "WV" , "WW" , "WX" , "WY" , "WZ" , "XA" , "XB" , "XC" , "XD" , "XE" , "XF" , "XG" , "XH" , "XI" , "XJ" , "XK" , "XL" , "XM" , "XN" , "XO" , "XP" , "XQ" , "XR" , "XS" , "XT" , "XU" , "XV" , "XW" , "XX" , "XY" , "XZ" , "YA" , "YB" , "YC" , "YD" , "YE" , "YF" , "YG" , "YH" , "YI" , "YJ" , "YK" , "YL" , "YM" , "YN" , "YO" , "YP" , "YQ" , "YR" , "YS" , "YT" , "YU" , "YV" , "YW" , "YX" , "YY" , "YZ" , "ZA" , "ZB" , "ZC" , "ZD" , "ZE" , "ZF" , "ZG" , "ZH" , "ZI" , "ZJ" , "ZK" , "ZL" , "ZM" , "ZN" , "ZO" , "ZP" , "ZQ" , "ZR" , "ZS" , "ZT" , "ZU" , "ZV" , "ZW" , "ZX" , "ZY" , "ZZ"]
    return alphabet[collumn]



"""
    string = "["
    for i in range(26):
        for j in range(26):
            string = string + f"\"{liste[i]}{liste[j]}\" , " # I used this to make the big list
    print(string + "]")""" 



def generateSetBGColorString(ID):                                                             #1 line, partially stollen from someone more competent than me
    return f"\x1b[48;5;{ID}m"

    #The table starts with the original 16 colors (0-15).
    #The proceeding 216 colors (16-231) or formed by a 3bpc RGB value offset by 16, packed into a single value.
    #The final 24 colors (232-255) are grayscale starting from a shade slighly lighter than black, ranging up to shade slightly darker than white.

def generateSetTextColorString(ID):                                                           #1 line, partially stollen from someone more competent than me
    return f"\x1b[38;5;{ID}m"


def resetBGColor():                                                                           #I think it doesn't work, unused

    color = "253"
    sys.stdout.write(f"\x1b[48;5;{color}m")
    sys.stdout.flush()


def invertDimentions(liste):                                                                  #copy-pasted from an old program, probably really stupid but tested a lot, should wwork
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
    




if __name__ == "__main__":
    from math import pi
    from random import randint
#    printScreen([[None if randint(0,6) == 0 else randint(0,25) for _ in range(50)] for _ in range(100)],randint(0,10),randint(0,10),randint(6,20),randint(10,50),randint(10,50))      #this ugly af thing genrerates a random spreadsheet for testing purposes
#    printScreen([[pi for _ in range(50)] for _ in range(50)],0,0,10,5,5)
 #   for i in range(16,231):
  #      print(generateSetBGColorString(SELECTEEDSQUARECOLOR) + generateSetTextColorString(i) + str(i))
    printScreen([[str(randint(1,19)) for _ in range(50)] for _ in range(10)],0,0,10,5,5,3)

