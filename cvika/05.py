def is_numeric(n: str) -> bool:
    try:
        float(n)
        return True
    except ValueError:
        return False


cars = ["Ford", "Audi", "Alfa Romeo", "Škoda", "Toyota", "Volvo"]


def contains(find: str, items: list[str]) -> bool:
    for item in items:
        if item == find:
            return True
    return False


def remove(find: str, items: list[str]) -> None:
    try:
        while True:
            items.remove(find)
    except:
        return None


def revert(items: list[str]) -> list[str]:
    result = []
    length = len(items)
    for i in range(length):
        result.append(items[length - i - 1])
    return result


print(cars)
print(revert(cars))