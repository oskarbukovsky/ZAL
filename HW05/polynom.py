def polyEval(poly, x):
    result = 0
    for i in range(len(poly)):
        result += poly[i] * x**i
    return result


# poly1 = [1, 2.5, 3.5, 0, 5.4]
# print(polyEval(poly1, 0))
# print(polyEval(poly1, 2))


def polySum(poly1, poly2):
    result = []
    high = poly1 if len(poly1) > len(poly2) else poly2
    low = poly2 if len(poly1) > len(poly2) else poly1
    for i in range(len(low)):
        result.append(poly1[i] + poly2[i])
    for i in range(len(high) - len(low)):
        result.append(high[len(low) + i])

    result.reverse()
    while result[0] == 0:
        result.pop(0)
    result.reverse()
    return result


# print(polySum([1, 2, 5], [2, 0, 1, -7]))
# print(polySum([1, 2.5, 3.5, 0, 5.4], [-1, -3.5, -3.5, 0, -5.4]))


def polyMultiply(poly1, poly2):
    # print("==================")
    pol1 = poly1
    pol2 = poly2
    # pol1.reverse()
    # pol2.reverse()
    result = [0] * ((len(pol1) + len(pol2)) - 1)
    for i in range(len(pol1)):
        for j in range(len(pol2)):
            # print("i: " + str(i) + " j: " + str(j) + " += " + str(pol1[i]) + "*" + str(pol2[j]))
            result[i + j] += pol1[i] * pol2[j]
    # result.reverse()
    return result

print(polyMultiply([1, 2, 5], [2, 0, 1, -7]))
print(polyMultiply([2, 1], [3, -1, 4]))
print(polyMultiply([1, -1, 2], [1, 0, -3]))