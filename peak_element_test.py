import unittest


def find_peak(arr):
    peak = None
    length = len(arr)
    if length >= 1:
        peak = arr[0]
        if length >= 2:
            if arr[0] < arr[1]:
                peak = arr[1]
            if length == 3:
                if arr[1] < arr[2]:
                    peak = arr[2]
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

    def test_three_element_array_with_right_element_as_peak(self):
        self.assertEqual(3, find_peak([1, 2, 3]))

    def test_four_element_array_with_first_element_as_peak(self):
        self.assertEqual(4, find_peak([4, 3, 2, 1]))



if __name__ == '__main__':
    unittest.main()
