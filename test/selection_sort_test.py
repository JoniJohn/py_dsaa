import allsorts

import unittest


class Test_SelectionSort(unittest.TestCase):
    def test_selection_sort_integer_asc(self):
        testArr = [3, 1, 2]
        expArr = [1, 2, 3]

        resArr = allsorts.selectionSortAsc(testArr)

        self.assertListEqual(expArr, resArr)

    def test_selection_sort_string_asc(self):
        testArr = ["John", "Jo", "Joh"]
        expArr = ["Jo", "Joh", "John"]

        resArr = allsorts.selectionSortAsc(testArr)

        self.assertListEqual(expArr, resArr)

    def test_selection_sort_integer_desc(self):
        testArr = [3, 1, 2]
        expArr = [3, 2, 1]

        resArr = allsorts.selectionSortDesc(testArr)

        self.assertListEqual(expArr, resArr)

    def test_selection_sort_string_desc(self):
        testArr = ["John", "Jo", "Joh"]
        expArr = ["John", "Joh", "Jo"]

        resArr = allsorts.selectionSortDesc(testArr)

        self.assertListEqual(expArr, resArr)


if __name__ == "__main__":
    unittest.main()
