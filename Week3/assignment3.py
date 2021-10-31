from typing import Any, Iterable


class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.prev: Node = None
        self.next: Node = None


class SimpleQueue:
    def __init__(self, iterable: Iterable[Any]) -> None:
        for value in iterable:
            self._tail = Node(value)
            try:
                self._tail.next = node
            except UnboundLocalError:
                node = self._tail
                self._head = node
            else:
                self._tail.next = node
                node.prev = self._tail
                node = self._tail

    def __bool__(self) -> bool:
        return self._head is not None

    def append(self, value: Any) -> None:
        raise NotImplementedError("Assignment 3 not complete")

    def popleft(self) -> Any:
        raise NotImplementedError("Assignment 3 not complete")
