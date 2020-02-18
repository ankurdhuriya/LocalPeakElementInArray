import unittest


def find_peak(arr):
    peak = None
    if len(arr) == 1:
        peak = arr[0]
    if len(arr) > 1:
        if arr[0] > arr[1]:
            peak = arr[0]
        if arr[0] < arr[1]:
            peak = arr[1]
    return peak


class MyTestCase(unittest.TestCase):
    def test_none_is_peak_element_for_null_array(self):
        self.assertEqual(None, find_peak([]))

    def test_single_element_array_have_that_element_as_peak(self):
        self.assertEqual(2, find_peak([2]))

    def test_two_element_array_with_left_element_as_peak(self):
        self.assertEqual(2, find_peak([2, 1]))

    def test_two_element_array_with_right_element_as_peak(self):
        self.assertEqual(2, find_peak([1, 2]))

    def test_three_element_array_with_left_element_as_peak(self):
        self.assertEqual(3, find_peak([3, 2, 1]))

    def test_three_element_array_with_middle_element_as_peak(self):
        self.assertEqual(3, find_peak([1, 3, 2]))


if __name__ == '__main__':
    unittest.main()
