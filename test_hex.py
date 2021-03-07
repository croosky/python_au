import unittest
from hex import Hex

class Test_Hex(unittest.TestCase):
    def test_add1(self):
        n1 = Hex("1111")
        n2 = Hex("")
        expect = "1111"
        result = printHex(n1.add(n2))
        self.assertEqual(expect, result)

    def test_add2(self):
        n1 = Hex("888")
        n2 = Hex("AB3")
        expect = "133B"
        result = printHex(n1.add(n2))
        self.assertEqual(expect, result)

    def test_add3(self):
        n1 = Hex("B")
        n2 = Hex("3456")
        expect = "3461"
        result = printHex(n1.add(n2))
        self.assertEqual(expect, result)

    def test_add4(self):
        n1 = Hex("8")
        n2 = Hex("21111")
        expect = "21119"
        result = printHex(n1.add(n2))
        self.assertEqual(expect, result)

    def test_add5(self):
        n1 = Hex("8")
        n2 = None
        expect = None
        result = printHex(n1.add(n2))
        self.assertEqual(expect, result)


def printHex(n):
    if not n:
        return None
    n = n.num
    result = ""
    while n:
        result += n.val
        n = n.next
    if result[0] == "0": result = result[1:]
    return result

if __name__ == "__main__":
    unittest.main()