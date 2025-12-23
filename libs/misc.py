#random useful fonctions


def isNumber(string):         #stupidely simple and tested
    for char in string:
        if not char in ("0","1","2","3","4","5","6","7","8","9"):
            return False

    return True


def strToBool(string):
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        raise TypeError(f"{string} is not convertible to a boolean")