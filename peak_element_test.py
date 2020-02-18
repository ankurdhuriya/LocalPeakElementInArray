import unittest


def find_peak(arr):
    if len(arr) == 1:
        return arr[0]
    return None


class MyTestCase(unittest.TestCase):
    def test_none_is_peak_element_for_null_array(self):
        self.assertEqual(None, find_peak([]))

    def test_single_element_array_have_that_element_as_peak(self):
        self.assertEqual(2, find_peak([2]))


if __name__ == '__main__':
    unittest.main()
