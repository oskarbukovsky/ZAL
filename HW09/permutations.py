from typing import Any


def permutations(
    array: list[Any],
    current: list[Any] = [],
    result: list[Any] = [],
    first: bool = True,
) -> list[Any]:
    if first:
        current = []
        result = []

    if len(array) < 1:
        result.append(current)
        return result

    for i in range(len(array)):
        permutations(array[:i] + array[i + 1 :], current + [array[i]], result, False)

    return result


# print(permutations([]))
# print("==========")
# print(permutations([1]))
# print("==========")
# print(permutations([1, 2]))
# print("==========")
# print(permutations([1, 2, 3]))
# print("==========")
# print(permutations(["a", "b", "c", "d"]))
# print("==========")
# print(permutations(['Skoda', 'Peugeot', 'BMW', 'Ford', 'Hyundai', 'Nissan']))
# print("==========")