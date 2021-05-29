import unittest
from main import filters
from main import str_to_dict


class TestSalesAnalysis(unittest.TestCase):
    def test_str_to_dict(self):
        data='date,resource,staff_id,count\n2020-06,3,1,12'
        result = str_to_dict(data)
        expect = {'date': '2020-06', 'resource': 3, 'staff_id': 1, 'count': 12}

        self.assertEqual(expect, result)

    def test_filters(self):
        l = [{'a': '1', 'b': '2'},{'a': '2', 'b': '2'}, {'a': '2', 'b': '1'}, {'a': '1', 'b': '1'}]
        key = 'a'
        val = 1

        result = filters(l, val, key)
        expect = [{'a': '1', 'b': '2'}, {'a': '1', 'b': '1'}]

        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()