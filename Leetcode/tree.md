# Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None: return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        return self.Traversal(root,result)

    def Traversal(self,root,result):
        if root==None: return None
        self.Traversal(root.left,result)
        result.append(root.val)
        self.Traversal(root.right,result)
        return result
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.result=[]
        self.c=0
        return self.Traversal(root,self.result)

    def next(self) -> int:
        number=self.result[self.c]
        self.c+=1
        return number

    def hasNext(self) -> bool:
        return len(self.result)>self.c

    def Traversal(self,root,result):
        if root==None: return None
        self.Traversal(root.left,result)
        result.append(root.val)
        self.Traversal(root.right,result)
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None: return root
        levels=[]
        level=[]
        queue = [root]
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left != None: queue.append(node.left)
                if node.right != None:queue.append(node.right)
            levels.append(level)
        return levels
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        counter=result=0
        stack = []
        stack.append(root)
        while counter < k:
            while root.left:
                root=root.left
                stack.append(root)
            root=stack.pop()
            counter+=1
            result=root.val
            while root.right == None:
                if counter == k:
                    return result
                root = stack.pop()
                counter += 1
                result = root.val
            root=root.right
            stack.append(root)
        return result
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
class Solution:
    def BST(self,root,mini,maxi):
        if root==None: return True
        if root.val<=mini or root.val>=maxi: return False
        return self.BST(root.left, mini, root.val) and self.BST(root.right, root.val,maxi)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.BST(root,float(-inf), float(inf))
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
class Solution:
    def isSymmetric2(self,root1,root2):
        if root1==None or root2==None: return root1==root2
        if root1.val!=root2.val: return False
        return self.isSymmetric2(root1.left,root2.right) and self.isSymmetric2(root1.right,root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None: return True
        return self.isSymmetric2(root.left,root.right)
```

