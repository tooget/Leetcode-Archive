# [1] Two Sum  

# https://leetcode.com/problems/two-sum/description/

# * algorithms
# * Easy (44.90%)
# * Source Code:       1.two-sum.0.py
# * Total Accepted:    2.4M
# * Total Submissions: 5.4M
# * Testcase Example:  '[2,7,11,15]\n9'

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:


# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def compareSumWithTarget():

            from itertools import count, combinations 
            numsIdx = range(0, len(nums))
            
            for i in numsIdx:
                for j in range(0, i):
                    if nums[i] + nums[j] == target:
                        yield i, j
        
        return list(next(compareSumWithTarget()))