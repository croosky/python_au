# Array

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
+ [Move Zeroes](#move-zeroes)
+ [Transpose Matrix](#transpose-matrix)
+ [Flipping an Image](#flipping-an-image)
+ [Image Smoother](#image-smoother)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Max Consecutive Ones](#max-consecutive-ones)

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[x*x for x in nums]
        return sorted(nums)
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=i=0
        while counter!=len(nums):
            if nums[i]==0:
                nums.append(nums.pop(i))
            else:
                i+=1
            counter+=1
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B=[[0]*len(A) for i in range(len(A[0]))]
        for i in range(len(A[0])):
            for j in range(len(A)):
                B[i][j]=A[j][i]
        return B
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A=[list(reversed(x)) for x in A]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0:
                    A[i][j]=1
                else:
                    A[i][j]=0
        return A
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows,columns=len(M),len(M[0])
        N=[]
        for i in range(rows):
            N.append([])
            for j in range(columns):
                top,bottom,left,right=i-1,i+1,j-1,j+1
                summ=M[i][j]
                count=1
                if top>=0:
                    summ+=M[top][j]
                    count+=1
                    if left>=0:
                        summ+=M[top][left]
                        count+=1
                    if right<columns:
                        summ+=M[top][right]
                        count+=1
                if bottom<rows:
                    summ+=M[bottom][j]
                    count+=1
                    if right<columns:
                        summ+=M[bottom][right]
                        count+=1
                    if left>=0:
                        summ+=M[bottom][left]
                        count+=1
                if right<columns:
                    summ+=M[i][right]
                    count+=1
                if left>=0:
                    summ+=M[i][left]
                    count+=1
                N[i].append(floor(summ/count))
        return N
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        l=[]
        nums_r,nums_c=len(nums),len(nums[0])
        if nums_r*nums_c!=r*c:
            return nums
        nums2=[[0]*c for i in range(r)]
        for i in range(nums_r):
            for j in range(nums_c):
                l.append(nums[i][j])
        it=0
        for i in range(r):
            for j in range(c):
                nums2[i][j]=l[it]
                it+=1
        return nums2
```

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k,maxk=0,0
        for i in nums:
            if i==1:
                k+=1
            else:
                if k>maxk:
                    maxk=k
                k=0
        if k>maxk:
            return k
        else:
            return maxk
```

