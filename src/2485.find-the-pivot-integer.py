#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#
# https://leetcode.com/problems/find-the-pivot-integer/description/
#
# algorithms
# Easy (83.79%)
# Likes:    1414
# Dislikes: 60
# Total Accepted:    290.4K
# Total Submissions: 346.4K
# Testcase Example:  '8'

# Given a positive integer n, find the pivot integer x such that:
# 
# 
# The sum of all elements between 1 and x inclusively equals the sum of all
# elements between x and n inclusively.
# 
# 
# Return the pivot integer x. If no such integer exists, return -1. It is
# guaranteed that there will be at most one pivot index for the given input.
# 
# 
# Example 1:
# 
# 
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8
# = 21.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# Explanation: 1 is the pivot integer since: 1 = 1.
# 
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: -1
# Explanation: It can be proved that no such integer exist.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        pvt_num = 0
        for i in range(n):
            pvt_num += i + 1
            if pvt_num == sum(range(i + 1, n + 1)):
                return i + 1
        return -1
# @lc code=end

