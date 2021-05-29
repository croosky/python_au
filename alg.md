+ [K Closest Points to Origin](#k-closest-points-to-origin)
+ [Merge k Sorted Lists](#Merge k Sorted Lists)
+ [Implement Queue using Stacks](#Implement Queue using Stacks)

## K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:k]
```

## Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

```python
class Solution(object):
    def mergeKLists(self, lists):
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
```
## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        return not self.s1
```

