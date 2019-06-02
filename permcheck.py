import unittest
import random

ARR_RANGE = (1, 100000)
INT_RANGE = (1, 1000000000)


def solution(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)
    """
    # an empty list is not a permutation
    if not len(A):
        return 0

    # track the hits with a dictionary
    hits = {}
    for item in A:
        # (quick exit) each element once and only once thanks
        if item in hits:
            return 0
        hits[item] = True

    # (quick exit again) each element once and only once
    if len(hits) != len(A):
        return 0

    # ok, see if they're all there
    for num in range(1, len(A) + 1):
        if num not in hits:
            return 0

    return 1

class TestExercise(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solution([4, 1, 3, 2]), 1)
        self.assertEqual(solution([4, 1, 3]), 0)

    def test_bottom_edge(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([1]), 1)
        self.assertEqual(solution([2]), 0)
        self.assertEqual(solution([1, 2]), 1)
        self.assertEqual(solution([2, 1]), 1)
        self.assertEqual(solution([2, 2]), 0)
        self.assertEqual(solution([1, 1]), 0)
        self.assertEqual(solution([1, 2, 3]), 1)
        self.assertEqual(solution([3, 2, 1]), 1)
        self.assertEqual(solution([5, 2, 1]), 0)
        self.assertEqual(solution([3, 1]), 0)

    def test_duplicates(self):
        self.assertEqual(solution([3, 3, 3, 3, 2, 1]), 0)

    def test_extreme(self):
        # full complement of numbers
        arr = list(range(*ARR_RANGE))
        random.shuffle(arr)
        self.assertEqual(solution(arr), 1)

        # full complement with one missing
        arr.remove(random.randint(1,len(arr)))
        self.assertEqual(solution(arr), 0)

if __name__ == '__main__':
     unittest.main()