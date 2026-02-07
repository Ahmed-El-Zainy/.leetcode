#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/
#
# algorithms
# Hard (36.55%)
# Likes:    2101
# Dislikes: 175
# Total Accepted:    77.6K
# Total Submissions: 211.5K
# Testcase Example:  '[9,3,5]'

# You are given an array target of n integers. From a starting array arr
# consisting of n 1's, you may perform the following procedure :
# 
# 
# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < n and set the value of arr at index i to
# x.
# You may repeat this procedure as many times as needed.
# 
# 
# Return true if it is possible to construct the target array from arr,
# otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: target = [9,3,5]
# Output: true
# Explanation: Start with arr = [1, 1, 1] 
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done
# 
# 
# Example 2:
# 
# 
# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].
# 
# 
# Example 3:
# 
# 
# Input: target = [8,5]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# n == target.length
# 1 <= n <= 5 * 10^4
# 1 <= target[i] <= 10^9
# 
# 
#
from typing import List
import heapq

# @lc code=start
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest
            
            if largest==1 or rest==1:
                return True

            if rest==0 and rest >= largest:
                return False
            prev = largest % rest
            
            if prev==0:
                return False
            heapq.heappush(heap, -prev)
            total = prev + rest
            
# @lc code=end



