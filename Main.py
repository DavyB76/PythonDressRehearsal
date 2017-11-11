import unittest


def OddSort(inputarray):

    oddarray  = []
    evenarray = []

    for nb in inputarray:
        if nb % 2 == 0:
            evenarray.append(nb)
        else:
            oddarray.append(nb)

    return evenarray + oddarray


class TestsOddArrayAlgo(unittest.TestCase):

    def test_ShouldReturnTwoBeforeOne_WhenArrayIsComposedOfOneAndTwo(self):
        actual = OddSort([1, 2])
        self.assertSequenceEqual(actual, [2, 1])

    def test_ShouldReturnTwoInFront_WhenArrayIsComposedOfOneTwoThreeFour(self):
        actual = OddSort([1, 2, 3, 4])
        self.assertSequenceEqual(actual, [2, 4, 1, 3])


def OddSortOneSpace(inputArray):
    return SwapEvenAfterOdd(inputArray, 0, len(inputArray) - 1)


def SwapEvenAfterOdd(inputArray, beginIndex, endIndex):
    if beginIndex == endIndex:
        return inputArray

    if inputArray[endIndex] % 2 == 0:
        inputArray[endIndex], inputArray[beginIndex] = inputArray[beginIndex], inputArray[endIndex]
        beginIndex += 1
    else:
        endIndex -= 1

    return SwapEvenAfterOdd(inputArray, beginIndex, endIndex)


class TestsOddArrayAlgo_OneSpace(unittest.TestCase):

    def test_ShouldReturnTwoBeforeOne_WhenArrayIsComposedOfOneAndTwo(self):
        actual = OddSortOneSpace([1, 2])
        self.assertSequenceEqual(actual, [2, 1])

    def test_ShouldReturnTwoInFront_WhenArrayIsComposedOfOneTwoThreeFour(self):
        actual = OddSortOneSpace([1, 3, 2, 4])
        self.assertSequenceEqual(actual, [4, 2, 3, 1])


if __name__ == '__main__':
    unittest.main()