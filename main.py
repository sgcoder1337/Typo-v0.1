import sys

begin = False
end = False

print("Typo v0.1")

def RaiseSyntaxError(text):
    """
    Raises a SyntaxError.
    """
    print(f"SyntaxError: {text}")
    sys.exit()

def RaiseTypeError(text):
    """
    Raises a TypeError.
    """
    print(f"TypeError:  {text}")
    sys.exit()

def RaiseIndentationError(text):
    """
    Raises an IndentationError.
    """
    
def Add(first, second):
    try:
        return first + second
    except TypeError:
        RaiseTypeError("Expected integers as arguments, found non-integer object")

def Subtract(first, second):
    try:
        return first - second
    except TypeError:
        RaiseTypeError("Expected integers as arguments, found non-integer object")

def Multiply(first, second):
    try:
        return first * second
    except TypeError:
        RaiseTypeError("Expected integers as arguments, found non-integer object")

def Divide(first, second):
    try:
        return first / second
    except TypeError:
        RaiseTypeError("Expected integers as arguments, found non-integer object")

def Interpreter():
    while True:
        code = input("> ")
        code = code.split(" ")
        
        # BEGIN and END code
        if "BEGIN" in code:
            begin = True
        elif "END" in code and begin == False:
            RaiseSyntaxError("Found keyword END before BEGIN")
        elif "END" in code and begin == True:
            end = True
        elif begin == False:
            RaiseSyntaxError("Expected keyword BEGIN at start, none found")
        else:
            continue
        if end == True:
            sys.exit()

        # Basic Math Operation code
        if "PADD" in code and index("PADD") == 1:
            print(Add(int(code[2]), int(code[3])))
        elif index("PADD") == 0:
            RaiseIndentationError("Expected one level of indentation, found none")
        elif index("PADD") != 1:
            RaiseIndentationError("Expected one level of indentation, found more")
        else:
            continue

        if "PSUBTRACT" in code and index("PSUBTRACT") == 1:
            print(Subtract(int(code[2]), int(code[3])))
        elif index("PSUBTRACT") == 0:
            RaiseIndentationError("Expected one level of indentation, found none")
        elif index("PSUBTRACT") != 1:
            RaiseIndentationError("Expected one level of indentation, found more")
        else:
            continue

        if "PMULTIPLY" in code and index("PMULTIPLY") == 1:
            print(Multiply(int(code[2]), int(code[3])))
        elif index("PMULTIPLY") == 0:
            RaiseIndentationError("Expected one level of indentation, found none")
        elif index("PMULTIPLY") != 1:
            RaiseIndentationError("Expected one level of indentation, found more")
        else:
            continue

        if "PDIVIDE" in code and index("PDIVIDE") == 1:
            print(Divide(int(code[2]), int(code[3])))
        elif index("PDIVIDE") == 0:
            RaiseIndentationError("Expected one level of indentation, found none")
        elif index("PDIVIDE") != 1:
            RaiseIndentationError("Expected one level of indentation, found more")
        else:
            continue
