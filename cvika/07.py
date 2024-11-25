from typing import Any
from __future__ import annotations
{   
# class Car:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand

#     def __str__(self) -> str:
#         return f"Car {self.brand} za {self.price}Kč"


# class Stack:
#     def __init__(self) -> None:
#         self.items: list[int] = []

#     def push(self, item) -> None:
#         self.items.append(item)

#     def pop(self) -> int:
#         return self.items.pop()

#     def size(self) -> int:
#         return len(self.items)

#     def is_empty(self) -> bool:
#         if self.size() == 0:
#             return True
#         else:
#             return False


# stack1 = Stack()

# for i in range(10):
#     stack1.push(3*i)

# print(stack1.size())

# for i in range(3):
#     print(stack1.pop())

# print(stack1.size())
}

class Node:
    def __init__(
        self,
        priority: int,
        data: Any,
        prevNode: Node | None = None,
        nextNode: Node | None = None,
    ):
        self.priority: int = priority
        self.data: Any = data
        self.nextNode: Node | None = nextNode
        self.prevNode: Node | None = prevNode

    def getPriority(self) -> int:
        return self.priority

    def getData(self) -> Any:
        return self.data


class LinkedList:
    def __init__(self) -> None:
        self.head: None | list[Node] = None

    def push(self, priority, data) -> None:
        newItem = Node(priority, data)
        if self.head == None:
            self.head = []
            self.head.append(newItem)

    def pop(self) -> Any:
        pass
