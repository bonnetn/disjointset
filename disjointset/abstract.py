import abc
import typing

SetID = typing.Hashable


class DuplicateIDException(Exception):
    """
    ID is already stored in the disjoint set.
    """


class AbstractDisjointSet(abc.ABC):
    @abc.abstractmethod
    def make_set(self, id: SetID) -> None:
        """
        Add a new disjoint set.
        Throws DuplicateIDException if called several times with the same ID.
        """

    @abc.abstractmethod
    def find(self, id: SetID) -> SetID:
        """
        Find the root element of the set.
        """

    @abc.abstractmethod
    def union(self, x: SetID, y: SetID) -> None:
        """
        Combine the two sets of x and y.
        """

    @property
    @abc.abstractmethod
    def size(self) -> int:
        """
        Return the disjoint set count.
        """
