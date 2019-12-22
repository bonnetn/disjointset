from __future__ import annotations

import typing
from abc import ABC

from disjointset.abstract import AbstractDisjointSet, SetID, DuplicateIDException
from disjointset.linked_list.tree import Node

UnionFunction = typing.Callable[[Node, Node], None]
FindFunction = typing.Callable[[Node], Node]


class AbstractLLDisjointSet(AbstractDisjointSet, ABC):
    """
    Disjoint set implementation with a tree represented as a linked list.

    Storage: LinkedList (Tree)
    """

    def __init__(self, union_func: UnionFunction, find_func: FindFunction):
        self._sets: typing.Dict[SetID, Node] = {}
        self._size = 0
        self._union = union_func
        self._find = find_func

    @property
    def size(self) -> int:
        return self._size

    def make_set(self, id: SetID) -> None:
        if id in self._sets:
            raise DuplicateIDException()

        n = Node(
            parent=None,
            id=id,
            rank=0,
            size=1,
        )
        n.parent = n
        self._sets[id] = n
        self._size += 1

    def find(self, id: SetID) -> SetID:
        return self._find(self._sets[id]).id

    def union(self, x: SetID, y: SetID) -> None:
        root_x = self._find(self._sets[x])
        root_y = self._find(self._sets[y])

        if root_x is root_y:
            return

        self._union(root_x, root_y)

        self._size -= 1


def get_linked_list_disjoint_set_class(union_func: UnionFunction, find_func: FindFunction):
    class LinkedListDisjointSet(AbstractLLDisjointSet):
        def __init__(self):
            super().__init__(union_func, find_func)

    return LinkedListDisjointSet
