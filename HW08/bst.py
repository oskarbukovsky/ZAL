from __future__ import annotations


class Node:
    def __init__(self: Node, value: int) -> None:
        self.value: int = value
        self.left: None | Node = None
        self.right: None | Node = None


class BinarySearchTree:
    def __init__(self: BinarySearchTree) -> None:
        self.data: Node | None = None
        self.visitedNodesCounter = 0

    def insert(self: BinarySearchTree, value: int) -> None:
        if self.data is None:
            self.data = Node(value)
        else:
            parent = self.walk(self.data, value)
            if parent is None:
                raise SystemError()
            if value < parent.value:
                parent.left = Node(value)
            elif value > parent.value:
                parent.right = Node(value)
            else:
                raise ValueError()

    def walk(self: BinarySearchTree, node: Node, value: int) -> Node | None:
        if value < node.value:
            if node.left is not None:
                return self.walk(node.left, value)
            else:
                return node
        elif value > node.value:
            if node.right is not None:
                return self.walk(node.right, value)
            else:
                return node
        raise ValueError()

    def fromArray(self: BinarySearchTree, array: list[int]):
        for i in range(len(array)):
            self.insert(array[i])

    def searchHelper(self: BinarySearchTree, node: Node | None, value: int):
        if node is None:
            return False
        self.visitedNodesCounter += 1
        if node.value == value:
            return True
        if node.value < value:
            if node.right is None:
                return False
            return self.searchHelper(node.right, value)
        else:
            if node.left is None:
                return False
            return self.searchHelper(node.left, value)

    def search(self: BinarySearchTree, value: int):
        self.visitedNodesCounter = 0
        return self.searchHelper(self.data, value)

    def min(self: BinarySearchTree) -> int | None:
        self.visitedNodesCounter = 0
        min: Node | None = None
        tmp: Node | None = self.data
        while tmp is not None:
            min = tmp
            tmp = tmp.left
            self.visitedNodesCounter += 1
        return min.value if min is not None else None

    def max(self: BinarySearchTree) -> int | None:
        self.visitedNodesCounter = 0
        max: Node | None = None
        tmp: Node | None = self.data
        while tmp is not None:
            max = tmp
            tmp = tmp.right
            self.visitedNodesCounter += 1
        return max.value if max is not None else None

    def visitedNodes(self: BinarySearchTree) -> int:
        return self.visitedNodesCounter

    def wait(self):
        return 1


# bst1 = BinarySearchTree()

# print(bst1.search(10))
# print(bst1.visitedNodes())
# print(bst1.min())
# print(bst1.max())

# bst2 = BinarySearchTree()
# bst2.fromArray([5, 3, 1, 4, 7, 6, 8])

# print(bst2.search(5))
# print(bst2.visitedNodes())
# print(bst2.search(7))
# print(bst2.visitedNodes())
# print(bst2.search(6))
# print(bst2.visitedNodes())
# print(bst2.search(10))
# print(bst2.visitedNodes())
# print("MIN: " + str(bst2.min()))
# print(bst2.visitedNodes())
# print("MAX: " + str(bst2.max()))
# print(bst2.visitedNodes())

# bst3 = BinarySearchTree()
# bst3.fromArray([1, 3, 4, 5, 6, 7, 8])

# print("MIN: " + str(bst3.min()))
# print(bst3.visitedNodes())
# print("MAX: " + str(bst3.max()))
# print(bst3.visitedNodes())