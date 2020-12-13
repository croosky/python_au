# Math

+ [Sqrt(x)](#sqrt(x))
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Fibonacci Number](#fibonacci-number)
+ [Base 7](#base-7)
+ [Fizz Buzz](#fizz-buzz)
+ [Palindrome Number](#palindrome-number)
+ [Reverse Integer](#reverse-integer)

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i+2]+A[i+1]>A[i]:
                return A[i]+A[i+1]+A[i+2]
        return 0
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        a=[0,1]
        for i in range(2, N+1):
            a.append(a[i-1]+a[i-2])
        return a.pop()

```

## Base 7

https://leetcode.com/problems/base-7/

```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num<0:
            minus=True
            num=-num
        elif num==0:
            return "0"
        else:
            minus=False
        s=''
        while num>0:
            q=int(num/7)
            s=s+str(num%7)
            num=q
        if minus:
            s=s+'-'
        return s[::-1]
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        FB=[]
        for i in range(1,n+1):
            if i%15==0:
                FB.append("FizzBuzz")
            elif i%3==0:
                FB.append("Fizz")
            elif i%5==0:
                FB.append("Buzz")
            else:
                FB.append(str(i))
        return FB
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        X=x
        reverse=0
        while x>0:
            reverse=10*reverse+x%10
            x=x//10
        if X==reverse:
            return True
        else:
            return False
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
class Solution:
    def reverse(self, x: int) -> int:
        y=int(str(abs(x))[::-1])
        if y.bit_length()>=32:
            return 0
        else:
            if x<0:
                return -y
            else:
                return y
```

