# Linked list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Sort List](#sort-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Linked List Cycle](#linked-list-cycle)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Reorder List](#reorder-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous=None
        current=head
        while current:
            nextt=current.next
            current.next=previous
            previous=current
            current=nextt
        return previous
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow=head
        fast=head
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next

        previous=None
        current=slow
        while current:
            nextt=current.next
            current.next=previous
            previous=current
            current=nextt

        while previous:
            if previous.val!=head.val:
                return False
            head=head.next
            previous=previous.next
        return True
```

## Sort List

https://leetcode.com/problems/sort-list/

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        head=ListNode()
        t=head
        while l1 and l2:
            if l1.val>l2.val:
                t.next=l2
                l2=l2.next
            else:
                t.next=l1
                l1=l1.next
            t=t.next
        if l1:
            t.next=l1
        else:
            t.next=l2
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        if (not head or not head.next):
            return head
        slow=fast=head
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.mergeTwoLists(left, right)
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        first, second = headA, headB
        l1 = l2 = 0
        while first:
            first = first.next
            l1 += 1
        while second:
            second = second.next
            l2 += 1
        first, second = headA, headB
        while l1 < l2:
            second = second.next
            l2 -= 1
        while l2 < l1:
            first = first.next
            l1 -= 1
        while first and second:
            if first == second:
                return first
            first = first.next
            second = second.next
        return None
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=fast=head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=fast=head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        t=head
        while l1 and l2:
            if l1.val>l2.val:
                t.next=l2
                l2=l2.next
            else:
                t.next=l1
                l1=l1.next
            t=t.next
        if l1:
            t.next=l1
        else:
            t.next=l2
        return head.next
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first=second=head
        while n!=0:
            first=first.next
            n-=1
        if first==None:
            return head.next
        while first.next:
            first=first.next
            second=second.next
        second.next=second.next.next
        return head
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
class Solution:
    def Reverse(self, head):
        previous=None
        current=head
        while current:
            nextt=current.next
            current.next=previous
            previous=current
            current=nextt
        return previous

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return head
        slow=fast=head0=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        reverse=self.Reverse(slow.next)
        slow.next=None
        t=ListNode()
        while reverse:
            t=head0.next
            head0.next=reverse
            head0=reverse
            reverse=t
```

