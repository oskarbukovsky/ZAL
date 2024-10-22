import math


def newtonPi(init):
    x = init
    while True:
        x1 = x - (math.sin(x))/(math.cos(x))
        if x1 == x:
            break
        x = x1
    return x

# print("================================")
# print("newtonPi(1): " + str(newtonPi(1)))
# print("newtonPi(2): " + str(newtonPi(2)))
# print("newtonPi(3): " + str(newtonPi(3)))
# print("newtonPi(4): " + str(newtonPi(4)))
# print("newtonPi(10): " + str(newtonPi(10)))
# print("newtonPi(100): " + str(newtonPi(100)))
# print("newtonPi(1000): " + str(newtonPi(1000)))
# print("newtonPi(10000): " + str(newtonPi(10000)))
# print("newtonPi(100000): " + str(newtonPi(100000)))
# print("newtonPi(1000000): " + str(newtonPi(1000000)))
# print("newtonPi(10000000): " + str(newtonPi(10000000)))
# print("newtonPi(100000000): " + str(newtonPi(100000000)))


def leibnizPi(iterations):
    result = 0
    sign = -1
    for i in range(iterations):
        tmp = 4 / ((2 * (i)) + 1)
        sign *= -1
        result += sign * tmp
    return result


def nilakanthaPiHelper(iteration):
    start = (iteration+1) * 2
    return start * (start + 1) * (start + 2)


def nilakanthaPi(iterations):
    sign = -1
    result = 3
    for i in range(iterations-1):
        tmp = 4 / nilakanthaPiHelper(i)
        sign *= -1
        result += sign * tmp
    return result
