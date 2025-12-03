#random useful fonctions


def isNumber(string):         #stupidely simple and tested
    for char in string:
        if not char in ("0","1","2","3","4","5","6","7","8","9"):
            return False

    return True
