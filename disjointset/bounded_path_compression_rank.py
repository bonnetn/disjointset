from __future__ import annotations

import typing

from disjointset.abstract import DuplicateIDException


class BoundedDisjointSetPathCompressionAndRank:
    """
    This is an implementation of a disjoint set optimized for integer IDs bounded by a maximum
    value.
    Instead of using a linked list to store the parents and ranks, we use arrays.
    """

    def __init__(self, max_id: int):
        self._parent_list: typing.List[typing.Optional[int]] = [None] * max_id
        self._rank: typing.List[int] = [0] * max_id
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    def make_set(self, id: int) -> None:
        if self._parent_list[id] is not None:
            raise DuplicateIDException()

        self._parent_list[id] = id
        self._size += 1

    def find(self, id: int) -> int:
        if id != self._parent_list[id]:
            self._parent_list[id] = self.find(self._parent_list[id])

        return self._parent_list[id]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self._rank[root_x] < self._rank[root_y]:
            root_x, root_y = root_y, root_x
        elif self._rank[root_x] == self._rank[root_y]:
            self._rank[root_x] += 1

        self._parent_list[root_y] = root_x
        self._size -= 1
