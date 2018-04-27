# In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of
#  a numeric array.
#
# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).
#
# The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays.
#  If there is no peak in the given array, then the output should be {pos: [], peaks: []}.
#
# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)
#
# All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.
#
# The first and last elements of the array will not be considered as peaks (in the context of a mathematical function,
# we don't know what is after and before and therefore, we don't know if it is a peak or not).
#
# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak,
# please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1])
# returns {pos: [1], peaks: [2]} (or equivalent in other languages)
#
# Have fun!

import unittest

# def pickPeaks(array):
#     localMaxima = array[0]
#     result = {"pos": [], "peaks":[]}
#     i2 = 0
#     for i in range(0, len(array) - 1):
#         if i >= i2:
#             if array[i] > localMaxima and isLaterPeakLesser(array, i):
#                 if isNextPeakGreater(array, i):
#                     continue
#                 else:
#                     localMaxima = array[i]
#                     result = updatePeaks(localMaxima, result, i)
#                     if isLaterPeakLesser(array, i):
#                         i2 = nextLowestPeakPosition(array, i)
#                         localMaxima = array[i2]
#     return result

def pickPeaks(array):
    result = {"pos": [], "peaks":[]}
    for i in range(0, len(array) - 1):
            if isleftless(array, i) and isRightEventuallyLess(array, i):
                result = updatePeaks(array[i], result, i)
    return result


def updatePeaks(localMaxima, result, position):
    result["peaks"].append(localMaxima)
    result["pos"].append(position)
    return result

def isleftless(array, position):
    if position != 0:
        if array[position - 1] < array[position]:
            return True
        else:
            return False
    else:
        False

def isRightEventuallyLess(array, position):
    if position != len(array) - 1:
        if array[position + 1] < array[position]:
            return True
        elif array[position + 1] > array[position]:
            return False
        else:
            return isRightEventuallyLess(array, position + 1)
    else:
        return False

def isNextPeakGreater(array, position):
    if position != len(array):
        if array[position + 1] > array[position]:
            return True
        else:
            return False
    else:
        return False

def isNextPeakLesser(array, position):
    if position != len(array):
        if array[position + 1] < array[position]:
            return True
        else:
            return False
    else:
        return False

def isLaterPeakLesser(array, position):
    if position != len(array) - 1:
        if array[position + 1] < array[position]:
            return True
        else:
            return isLaterPeakLesser(array, position + 1)
    else:
        return False

def nextLowestPeakPosition(array, position):
    if position != len(array) - 1:
        if array[position + 1] < array[position]:
            return nextLowestPeakPosition(array, position + 1)
        else:
            return position
    else:
        return position

def nextHighestPeakPosition(array, position):
    if position != len(array) - 1:
        if array[position + 1] > array[position]:
            return nextLowestPeakPosition(array, position + 1)
        else:
            return position
    else:
        return position



class TestMethods(unittest.TestCase):

    def test_single_peak(self):
        self.assertEqual(pickPeaks([0, 1, 0]), {"pos": [1], "peaks": [1]})

    def test_no_peaks(self):
        self.assertEqual(pickPeaks([2, 2, 2]), {"pos": [], "peaks": []})

    def test_two_peaks(self):
        self.assertEqual(pickPeaks([0, 1, 0, 1, 0]), {"pos": [1, 3], "peaks": [1, 1]})

    def test_plateau_peaks(self):
        self.assertEqual(pickPeaks([0, 1, 2, 2, 2, 0]), {"pos": [2], "peaks": [2]})

    def test_multiple_peaks_and_plateaus(self):
        self.assertEqual(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {"pos": [3, 7, 10], "peaks": [6, 3, 2]})

    def test_high_inital_peak(self):
        self.assertEqual(pickPeaks([9, 1, 1, 1, 2, 1]), {"pos": [4], "peaks": [2]})


    # Later Peak Test

    def test_later_peak_lesser_true(self):
        self.assertEqual(isLaterPeakLesser([0, 1, 2, 2, 2, 0], 2), True)

    def test_later_peak_lesser_false(self):
        self.assertEqual(isLaterPeakLesser([0, 1, 2, 2, 2, 2], 2), False)

    # Next Lowest Position

    def test_next_lowest_peak_position(self):
        self.assertEqual(nextLowestPeakPosition([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1], 3), 5)

    def test_next_lowest_peak_position_plateau(self):
        self.assertEqual(nextLowestPeakPosition([3, 2, 3, 6, 4, 1, 2, 4, 3, 2, 2, 2, 3, 2, 1], 7), 9)

if __name__ == '__main__':
    unittest.main()


# def pick_peaks(arr):
#     pos = []
#     prob_peak = False
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             prob_peak = i
#         elif arr[i] < arr[i-1] and prob_peak:
#             pos.append(prob_peak)
#             prob_peak = False
#     return {'pos':pos, 'peaks':[arr[i] for i in pos]}

# def pick_peaks(arr):
#     peak, pos = [], []
#     res = {"peaks": [], "pos": []}
#
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             peak, pos = [arr[i]], [i]
#
#         elif arr[i] < arr[i - 1]:
#             res["peaks"] += peak
#             res["pos"] += pos
#             peak, pos = [], []
#
#     return res