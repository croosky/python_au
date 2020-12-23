class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return '{}'.format(self.val)

class Hex:
    def __init__(self,n=None):
        if n!= n.upper():
            print("Letters should be capital.")
            return None
        number=Linked()
        for i in n:
            number.addNode(i)
        self.num=number.head

    def from16to10(self,n):
        if n >= 'A' and n <= 'F':
            return ord(n) - ord('A') + 10
        return ord(n) - ord('0')

    def from10to16(self,n):
        if n > 9:
            return chr(ord('A') + n - 10)
        return chr(ord('0') + n)

    def add(self,n2):
        if not n2:
            return None
        n1=self.num
        n2=n2.num
        count=0
        result=""
        while n1 and n2:
            first=self.from16to10(n1.val)
            second=self.from16to10(n2.val)
            summ=first+second+count
            if summ<16:
                result+=self.from10to16(summ)
                count=0
            else:
                result+=self.from10to16(summ-16)
                count=1
            n1,n2=n1.next,n2.next
        while n1:
            first = self.from16to10(n1.val)
            summ=first+count
            if summ<16:
                result+=self.from10to16(summ)
                count=0
            else:
                result+=self.from10to16(summ-16)
                count=1
            n1=n1.next
        while n2:
            second = self.from16to10(n2.val)
            summ=second+count
            if summ<16:
                result+=self.from10to16(summ)
                count=0
            else:
                result+=self.from10to16(summ-16)
                count=1
            n2=n2.next
        result+=str(count)
        return Hex(result[::1])
    def printHex(self):
        n=self.num
        result=""
        while n:
            result+=n.val
            n=n.next
        if result[0]=="0": result=result[1:]
        print(result)


class Linked:
    def __init__(self, head = None):
        self.head = head

    def addNode(self, val):
        cur = self.head
        new = Node(val)
        new.next = cur
        self.head = new


def main():
    number1, number2=Hex("31F"), Hex("13")
    summa=number1.add(number2)
    number1.printHex()
    number2.printHex()
    summa.printHex()

if __name__ == "__main__":
    main()