"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        res_dict = {}
        for i, v in enumerate(nums):

            minus = target - v
            if v not in res_dict:
                res_dict[minus] = i
            else:
                return [i, res_dict[minus]]


# 1 two sum finished, not understand totally yet
