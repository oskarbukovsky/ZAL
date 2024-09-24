def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if x == y:
        ValueError('This operation is not supported for given input parameters')
    return x / y

def modulo(x, y):
    return x % y

def secondPower(x):
    return x * x

def power(x, y):
    return float(x ** y)

def secondRadix(x):
    if x <= 0:
        ValueError('This operation is not supported for given input parameters')
    return x ** 1/2

def magic(x, y, z, k):
    l = x + k
    m = y + z
    if m == 0:
        ValueError('This operation is not supported for given input parameters')
    n = (l/m) + 1
    return n


def control(a, x, y, z, k):
    match a:
        case "ADDITION":
            addition()
        case "SUBTRACTION":
            subtraction()
        case "MULTIPLICATION":
            multiplication()
        case "DIVISION":
            division()
        case "MOD":
            modulo()
        case "POWER":
            power() 
        case "SECONDRADIX":
            secondRadix()
        case "MAGIC":
            magic()