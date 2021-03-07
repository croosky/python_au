import unittest
from md_generator import *

class Test(unittest.TestCase):

    def test_get_title(self):
        file = read_all_lines("test.txt")
        source = Solution(file[0], file[1], file[2:])
        result = source.get_title()
        expect = "##Insert Interval"
        self.assertEqual(result, expect)

    def test_read_all_lines(self):
        result = read_all_lines("test.txt")
        expect = ['57. Insert Interval\n', 'https://leetcode.com/problems/insert-interval/\n', 'class Solution:']
        self.assertEqual(result, expect)

    def test_merge(self):
        old = 'old_start \n[comment]: <> (Stop)\nold_end'
        new = 'new_start \n[comment]: <> (Stop)\nnew_end'
        result = merge(old, new)
        expect = 'old_start new_start \n[comment]: <> (Stop)\nold_endnew_end'
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()