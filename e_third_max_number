class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    """
      https://leetcode.com/problems/third-maximum-number/
      Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
    """
        set_nums = set(nums)
        l_nums_sorted = sorted(list(set_nums))
        if len(l_nums_sorted) >= 3:
            return l_nums_sorted[-3:][0]
        else:
            return l_nums_sorted[-1:][0]
        
