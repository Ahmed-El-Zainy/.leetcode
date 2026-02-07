#
# @lc app=leetcode id=3683 lang=python3
#
# [3683] Earliest Time to Finish One Task
#
# https://leetcode.com/problems/earliest-time-to-finish-one-task/description/
#
# algorithms
# Easy (83.69%)
# Likes:    43
# Dislikes: 2
# Total Accepted:    63.5K
# Total Submissions: 75.3K
# Testcase Example:  '[[1,6],[2,3]]'
#
# You are given a 2D integer array tasks where tasks[i] = [si, ti].
# 
# Each [si, ti] in tasks represents a task with start time si that takes ti
# units of time to finish.
# 
# Return the earliest time at which at least one task is finished.
# 
# 
# Example 1:
# 
# 
# Input: tasks = [[1,6],[2,3]]
# 
# Output: 5
# 
# Explanation:
# 
# The first task starts at time t = 1 and finishes at time 1 + 6 = 7. The
# second task finishes at time 2 + 3 = 5. You can finish one task at time 5.
# 
# 
# Example 2:
# 
# 
# Input: tasks = [[100,100],[100,100],[100,100]]
# 
# Output: 200
# 
# Explanation:
# 
# All three tasks finish at time 100 + 100 = 200.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tasks.length <= 100
# tasks[i] = [si, ti]
# 1 <= si, ti <= 100
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([x+y for x, y in tasks]) if tasks else 0

# @lc code=end

