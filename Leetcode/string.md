# String

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/submissions/

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Letters={}
        s=[x for x in s]
        t=[x for x in t]
        while s:
            temp=s.pop()
            if not temp in Letters:
                Letters[temp]=1
            else:
                Letters[temp]+=1
        while t:
            temp=t.pop()
            if temp in Letters:
                Letters[temp]-=1
            else:
                return False
        for l in Letters.values():
            if l!=0:
                return False
        return True
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i,c in enumerate(s):
            s.insert(0,s.pop(i))
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='AEIOUaeiou'
        vowels_s=[]
        for letter in s:
            if letter in vowels:
                vowels_s.append(letter)
        new_s=''
        for letter in s:
            if letter in vowels:
                new_s=new_s+vowels_s.pop()
            else:
                new_s=new_s+letter
        return new_s
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])
```

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
```

