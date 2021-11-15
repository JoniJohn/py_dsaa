import allsorts

import unittest


class Test_BubbleSort(unittest.TestCase):
    def test_bubble_sort_integer_arr_asc(self):
        # arrange
        testArr = [3, 1, 2]
        expArr = [1, 2, 3]
        # act
        resArr = allsorts.bubbleSortAsc(testArr)
        # assert
        self.assertListEqual(expArr, resArr)

    def test_bubble_sort_string_arr_asc(self):
        # arrange
        testArr = ["John", "Jo", "Joh"]
        expArr = ["Jo", "Joh", "John"]
        # act
        resArr = allsorts.bubbleSortAsc(testArr)
        # assert
        self.assertListEqual(expArr, resArr)

    def test_bubble_sort_int_arr_desc(self):
        # arrange
        testArr = [3, 1, 2]
        expArr = [3, 2, 1]
        # act
        resArr = allsorts.bubbleSortDesc(testArr)
        # assert
        self.assertListEqual(expArr, resArr)

    def test_bubble_sort_string_arr_desc(self):
        # arrange
        testArr = ["John", "Jo", "Joh"]
        expArr = ["John", "Joh", "Jo"]
        # act
        resArr = allsorts.bubbleSortDesc(testArr)
        # assert
        self.assertListEqual(expArr, resArr)


if __name__ == "__main__":
    unittest.main()
