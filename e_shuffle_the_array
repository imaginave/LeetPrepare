class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
            https://leetcode.com/problems/shuffle-the-array/
            Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
            Return the array in the form [x1,y1,x2,y2,...,xn,yn].
        """
        result : List[int] = []
        i = 0
        while i < n:
            y = i + n 
            result.append(nums[i])
            result.append(nums[y])
            i += 1
        return result
