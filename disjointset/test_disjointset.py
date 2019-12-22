import itertools

import pytest

from disjointset import DuplicateIDException, get_linked_list_disjoint_set_class, UNION_SIZE, \
    FIND_PATH_SPLITTING
from disjointset.linked_list import UNION_NAIVE, FIND_NAIVE, UNION_RANK, FIND_PATH_COMPRESSION, \
    FIND_PATH_HALVING

test_cases = list(itertools.product((UNION_NAIVE, UNION_RANK, UNION_SIZE),
                                    (FIND_NAIVE, FIND_PATH_COMPRESSION, FIND_PATH_HALVING, FIND_PATH_SPLITTING)))


@pytest.mark.parametrize('union_func,find_func', test_cases)
class TestDisjointSet:
    @pytest.fixture
    def disjoint_set(self, union_func, find_func):
        cls = get_linked_list_disjoint_set_class(union_func, find_func)
        return cls()

    def test_make_set_twice(self, disjoint_set):
        """
        Calling MakeSet twice with the same ID should throw an exception.
        """
        disjoint_set.make_set("id")
        with pytest.raises(DuplicateIDException):
            disjoint_set.make_set("id")

    def test_union_several_times(self, disjoint_set):
        """
        Calling union several on the same IDs pair should not fail.
        """
        disjoint_set.make_set(1)
        disjoint_set.make_set(2)

        disjoint_set.union(1, 2)
        disjoint_set.union(1, 2)
        disjoint_set.union(2, 1)

        assert disjoint_set.find(1), disjoint_set.find(2) in ((1, 1), (2, 2))

    def test_disjoint_set_size(self, disjoint_set):
        assert disjoint_set.size == 0

        disjoint_set.make_set(1)
        assert disjoint_set.size == 1

        disjoint_set.make_set(2)
        assert disjoint_set.size == 2

        disjoint_set.union(1, 2)
        assert disjoint_set.size == 1

        disjoint_set.make_set(3)
        assert disjoint_set.size == 2

        disjoint_set.union(2, 3)
        assert disjoint_set.size == 1

    def test_disjoint_set_find(self, disjoint_set):
        """
        Given 3 groups of IDs (in a union), "find" should find the disjoint sets.
        """
        group_list = [[1, 2, 3], [4, 5], [6]]
        for group in group_list:
            for element in group:  # Make all the sets.
                disjoint_set.make_set(element)

            for i in range(len(group) - 1):  # Union all the groups elements together.
                disjoint_set.union(group[i], group[i + 1])

        for group in group_list:
            # Find for each element in the group and store the result in a list.
            find_results = [disjoint_set.find(element) for element in group]

            # For the group [1,2,3], find_result must be either [1,1,1], [2,2,2] or [3,3,3].
            # Expected find result contains all potential valid results.
            valid_results_list = [[element] * len(group) for element in group]

            # Make sure that the result is valid.
            assert find_results in valid_results_list
