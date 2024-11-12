import random


def isSorted(data, condition):
    for i in range(len(data) - 1):
        if condition == "ASC":
            if data[i] > data[i + 1]:
                return False
        else:
            if data[i] < data[i + 1]:
                return False
    return True


def bogoSort(data):
    for i in range(len(data)):
        j = random.randint(0, len(data) - 1)
        data[i], data[j] = data[j], data[i]


# def sortNumbers(data, condition):
#     while not isSorted(data, condition):
#         bogoSort(data)
#     return data


def sortNumbers(data, condition):
    return mySort(condition, data)


def mySort(condition, data, weights=None):
    if weights == None:
        weights = data
    data = data.copy()
    weights = weights.copy()
    if condition == "ASC":
        for i in range(len(weights)):
            for j in range(i):
                if weights[i - j] < weights[i - j - 1]:
                    # print(1)
                    weights[i - j], weights[i - j - 1] = (
                        weights[i - j - 1],
                        weights[i - j],
                    )
                    data[i - j], data[i - j - 1] = data[i - j - 1], data[i - j]
    else:
        for i in range(len(weights)):
            for j in range(i):
                if weights[i - j] > weights[i - j - 1]:
                    # print(2)
                    weights[i - j], weights[i - j - 1] = (
                        weights[i - j - 1],
                        weights[i - j],
                    )
                    data[i - j], data[i - j - 1] = data[i - j - 1], data[i - j]
    # print(weights)
    # print(data)
    return data


def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError("Invalid input data")
    return mySort(condition, data, weights)


print(sortNumbers([100, 10, 90, 20, 80, 30, 70, 40, 60, 50], "ASC"))
print(sortNumbers([100, 10, 90, 20, 80, 30, 70, 40, 60, 50], "DESC"))

print(sortData([2, 5, 6, 1], ["Ford", "BMW", "Audi", "Volvo"], "ASC"))
print(sortData([2, 5, 6, 1], ["Ford", "BMW", "Audi", "Volvo"], "DESC"))
