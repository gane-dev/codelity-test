import unittest
from longestchain import Pair,LongChain
import random

class TestExercise(unittest.TestCase):

    def test_example(self):
        befarr = [(15, 25), (5, 24), (27, 40), (50, 60), (), (0, 0)]
        arr = LongChain.createArr(befarr)
        self.assertEqual(LongChain.solution(arr), 4)

    def test_random_example(self):
        befarr = [(random.randint(0, 100), random.randint(0, 100)) for k in range(10)]
        arr = LongChain.createArr(befarr)
        res = LongChain.solution(arr)
        self.assertEqual(LongChain.solution(arr), res)

    def test_negative_example(self):
        befarr = [(random.randint(-100, 100), random.randint(-100, 100)) for k in range(10)]
        arr = LongChain.createArr(befarr)
        res = LongChain.solution(arr)
        self.assertEqual(LongChain.solution(arr), res)

    # def test_large_random_example(self):
    #     befarr = [(random.randint(0, 100), random.randint(0, 100)) for k in range(10000)]
    #     arr = LongChain.createArr(befarr)
    #     res = LongChain.solution(arr)
    #     self.assertEqual(LongChain.solution(arr), res)
    #
    # def test_large_negative_example(self):
    #     befarr = [(random.randint(-100, 100), random.randint(-100, 100)) for k in range(10000)]
    #     arr = LongChain.createArr(befarr)
    #     res = LongChain.solution(arr)
    #     self.assertEqual(LongChain.solution(arr), res)

    def test_repeat(self):
        befarr = [(1, 1) for k in range(100)]
        arr = LongChain.createArr(befarr)
        res = LongChain.solution(arr)
        # print(res)
        self.assertEqual(LongChain.solution(arr), res)

    def test_10s_repeat(self):
        befarr = [(1, 0) for k in range(100)]
        arr = LongChain.createArr(befarr)
        res = LongChain.solution(arr)
        # print(res)
        self.assertEqual(LongChain.solution(arr), res)

    def test_01s_repeat(self):
        befarr = [(0, 1) for k in range(100)]
        arr = LongChain.createArr(befarr)
        res = LongChain.solution(arr)
        print(res)
        self.assertEqual(LongChain.solution(arr), res)

# arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]

    # arr = [Pair(15, 25),Pair(5, 24),  Pair(27, 40), Pair(50, 60)]

    # print('Length of maximum size chain is', maxLength(arr))
    # arr = [Pair(15, 25)]
    # print('Length of maximum size chain is', maxLength(arr))
    # arr = [Pair()]
    # print('Length of maximum size chain is', maxLength(arr))