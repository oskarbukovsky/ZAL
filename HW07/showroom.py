from __future__ import annotations


class Node:
    def __init__(
        self: Node, nextNode: Node | None, prevNode: Node | None, data: Car
    ) -> None:
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data


class LinkedList:
    def __init__(self: LinkedList) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None


class Car:
    def __init__(
        self: Car, identification: int, name: str, brand: str, price: int, active: bool
    ) -> None:
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars: list[Car | None]) -> None:
    for i in range(len(cars)):
        # print("== Adding [", cars[i].identification, "]==")
        add(cars[i])
        
def init1(cars: list[Car | None]) -> None:
    for i in range(len(cars)):
        # print("== Adding [", cars[i].identification, "]==")
        add1(cars[i])


def add1(car: Car | None) -> None:
    if not isinstance(car, Car):
        return
    # if find(car.identification) is not None:
    #     return
    if db.tail is None:
        db.head = Node(None, None, car)
        db.tail = db.head
        return

    newNode: Node = Node(None, db.tail, car)
    db.tail.nextNode = newNode
    db.tail = newNode

    tmp: Node | None = newNode
    # dbPrint()
    while (
        (tmp is not None)
        and (tmp.prevNode is not None)
        and (tmp.data.price < tmp.prevNode.data.price)
    ):

        tmp.data, tmp.prevNode.data = tmp.prevNode.data, tmp.data

        # print("Swap ", car.price, " < ", tmp.data.price)

        tmp = tmp.prevNode
    # dbPrint()


def add(car: Car | None) -> None:
    if not isinstance(car, Car):
        return
    if find(car.identification) is not None:
        return
    if not isinstance(db.head, Node):
        newNode:Node = Node(None, None, car)
        db.head = newNode
        db.tail = newNode
        # print("== End - First node ==")
        # dbPrint()
        return
    tmp: Node = db.head

    while True:
        if tmp.data.price > car.price: 
            if tmp.prevNode == None:  
                newNode = Node(tmp, None, car)
                db.head = newNode
            else:
                newNode = Node(tmp, tmp.prevNode, car)
                tmp.prevNode.nextNode = newNode # type: ignore
            tmp.prevNode = newNode
            return
        if not isinstance(tmp.nextNode, Node):  
            newNode = Node(None, tmp, car)
            tmp.nextNode = newNode
            return
        tmp = tmp.nextNode

    # print("== End ==")
    # dbPrint()


def find(identification: int) -> Node | None:
    tmp: Node | None = db.head
    while True:
        if tmp is None:
            return tmp
        if tmp.data.identification == identification:
            return tmp
        tmp = tmp.nextNode


def updateName(identification: int, name: str) -> None:
    node: Node | None = find(identification)
    if node is None:
        return
    node.data.name = name


def updateBrand(identification: int, brand: str) -> None:
    node: Node | None = find(identification)
    if node is None:
        return
    node.data.brand = brand


def activateCar(identification: int) -> None:
    node: Node | None = find(identification)
    if node is None:
        return
    node.data.active = True


def deactivateCar(identification: int) -> None:
    node: Node | None = find(identification)
    if node is None:
        return
    node.data.active = False


def getDatabaseHead() -> Node | None:
    return db.head


def getDatabase() -> LinkedList:
    return db


def calculateCarPrice() -> int:
    if db.head is None:
        return 0
    sum: int = 0
    tmp: Node | None = db.head
    while tmp is not None:
        if tmp.data.active:
            sum += tmp.data.price
        tmp = tmp.nextNode
    return sum


def clean() -> None:
    db.head = None
    db.tail = None


def dbPrint() -> None:
    print("== Printing DB: ==")
    tmp: Node | None = db.head
    if tmp is None:
        print("== Print End ==")
        return
    while True:
        print(
            "ID: ",
            str(tmp.data.identification),
            " \tName: ",
            str(tmp.data.name),
            " \tBrand: ",
            str(tmp.data.brand),
            "   \tPrice: ",
            str(tmp.data.price),
            " \tActive: ",
            str(tmp.data.active),
        )
        tmp = tmp.nextNode
        if tmp is None:
            break
    print("== Print End ==")


# init(
#     [
#         Car(1, "A8", "Audi", 5500, False),
#         Car(2, "xc90", "Volvo", 4700, True),
#         Car(1, "A8", "Audi", 5500, False),
#         Car(20, "ex30", "Volvo", 4700, True),
#         Car(3, "Veyron", "Bugatti", 19000, True),
#         Car(200, "v70", "Volvo", 4700, True),
#         None,
#         Car(4, "Fabia", "Škoda", 1250, False),
#         Car(300, "Divo", "Bugatti", 21400, True),
#         Car(30, "Chiron", "Bugatti", 19500, True),
#         Car(40, "Karoq", "Škoda", 1333, True),
#     ]
# )

# add1(Car(1, "A8", "Audi", 5500, False))
# add1(Car(2, "xc90", "Volvo", 4700, True))
# add1(Car(1, "A8", "Audi", 5500, False))
# add1(Car(20, "ex30", "Volvo", 4700, True))
# add1(Car(3, "Veyron", "Bugatti", 19000, True))
# add1(Car(200, "v70", "Volvo", 4700, True))
# add1(None)
# add1(Car(4, "Fabia", "Škoda", 1250, False))
# add1(Car(300, "Divo", "Bugatti", 21400, True))
# add1(Car(30, "Chiron", "Bugatti", 19500, True))
# add1(Car(40, "Karoq", "Škoda", 1333, True))

# add(Car(251, "S90", "Volvo", 4800, True))
# add(Car(5, "Q7", "Audi", 5800, True))
# add(Car(6, "XC60", "Volvo", 4600, False))
# add(Car(7, "A6", "Audi", 5400, False))
# add(Car(25, "C40", "Volvo", 5000, True))
# add(Car(26, "C40", "Volvo", 6000, True))
# add(Car(27, "C40", "Volvo", 5000, True))
# add(Car(8, "Chiron Sport", "Bugatti", 20000, True))
# add(Car(250, "S90", "Volvo", 4800, True))
# add(None)
# add(Car(10, "Octavia", "Škoda", 1350, False))
# add(Car(320, "Bolide", "Bugatti", 22000, True))
# add(Car(35, "Centodieci", "Bugatti", 21000, True))
# add(Car(50, "Superb", "Škoda", 1400, True))
# add(Car(252, "S90", "Volvo", 4800, True))


# deactivateCar(20)
# activateCar(4)
# updateBrand(200, "vOLVO")
# updateName(4, "Fabka")
# dbPrint()
# print("######## Total price: ", str(calculateCarPrice()), "########")
# clean()

# init1(
#     [
#         Car(1, "A8", "Audi", 5500, False),
#         Car(2, "xc90", "Volvo", 4700, True),
#         Car(1, "A8", "Audi", 5500, False),
#         Car(20, "ex30", "Volvo", 4700, True),
#         Car(3, "Veyron", "Bugatti", 19000, True),
#         Car(200, "v70", "Volvo", 4700, True),
#         None,
#         Car(4, "Fabia", "Škoda", 1250, False),
#         Car(300, "Divo", "Bugatti", 21400, True),
#         Car(30, "Chiron", "Bugatti", 19500, True),
#         Car(40, "Karoq", "Škoda", 1333, True),
#     ]
# )
# deactivateCar(20)
# activateCar(4)
# updateBrand(200, "vOLVO")
# updateName(4, "Fabka")
# dbPrint()
# print("######## Total price: ", str(calculateCarPrice()), "########")
