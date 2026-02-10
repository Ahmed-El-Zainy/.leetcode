#
# @lc app=leetcode id=3719 lang=python3
#
# [3719] Longest Balanced Subarray I
#
# https://leetcode.com/problems/longest-balanced-subarray-i/description/
#
# algorithms
# Medium (52.14%)
# Likes:    255
# Dislikes: 27
# Total Accepted:    67K
# Total Submissions: 109.7K
# Testcase Example:  '[2,5,4,3]'
#
# You are given an integer array nums.
# 
# A subarray is called balanced if the number of distinct even numbers in the
# subarray is equal to the number of distinct odd numbers.
# 
# Return the length of the longest balanced subarray.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,5,4,3]
# 
# Output: 4
# 
# Explanation:
# 
# 
# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3].
# Thus, the answer is 4.
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,2,5,4]
# 
# Output: 5
# 
# Explanation:
# 
# 
# The longest balanced subarray is [3, 2, 2, 5, 4].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5].
# Thus, the answer is 5.
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,2]
# 
# Output: 3
# 
# Explanation:
# 
# 
# The longest balanced subarray is [2, 3, 2].
# It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the
# answer is 3.
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1500
# 1 <= nums[i] <= 10^5
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            even, odd = set(), set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else: 
                    odd.add(nums[j])
                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)
        return ans
# @lc code=end

