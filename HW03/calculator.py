import math


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError("This operation is not supported for given input parameters")
    return x / y


def modulo(x, y):
    if x < y:
        raise ValueError("This operation is not supported for given input parameters")
    if y <= 0:
        raise ValueError("This operation is not supported for given input parameters")
    return x % y


def secondPower(x):
    return x * x


def power(x, y):
    if y < 0:
        raise ValueError("This operation is not supported for given input parameters")
    return float(x**y)


def secondRadix(x):
    try:
        if x<=0:
            raise ValueError("This operation is not supported for given input parameters")
        result = x**(1/2)
    except: 
        raise ValueError("This operation is not supported for given input parameters")
    return result

# print("secondRadix 0:", secondRadix(0))
# print("secondRadix 1:", secondRadix(-1.0))
# print("secondRadix 1:", secondRadix(-1))
# print("secondRadix 1:", secondRadix("-1"))
# print("secondRadix 1:", secondRadix("1"))
# print("secondRadix 2:", secondRadix(2))
# print("secondRadix 3:", secondRadix(3))
# print("secondRadix 4:", secondRadix(4))
# print("secondRadix 4.5:", secondRadix(4.5))


def magic(x, y, z, k):
    l = x + k
    m = y + z
    if m == 0:
        raise ValueError("This operation is not supported for given input parameters")
    n = (l / m) + 1
    return n


def control(a, x, y, z, k):
    match a:
        case "ADDITION":
            return addition(x, y)
        case "SUBTRACTION":
            return subtraction(x, y)
        case "MULTIPLICATION":
            return multiplication(x, y)
        case "DIVISION":
            return division(x, y)
        case "MOD":
            return modulo(x, y)
        case "POWER":
            return power(x, y)
        case "SECONDRADIX":
            return secondRadix(x)
        case "MAGIC":
            return magic(x, y, z, k)
        case _:
            raise ValueError(
                "This operation is not supported for given input parameters"
            )


# print("control: ", control("SECONDRADIX", 1, 3, 4, 5))
