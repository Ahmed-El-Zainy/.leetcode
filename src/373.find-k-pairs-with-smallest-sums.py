#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (41.26%)
# Likes:    6854
# Dislikes: 494
# Total Accepted:    430.4K
# Total Submissions: 1M
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing
# order and an integer k.
# 
# Define a pair (u, v) which consists of one element from the first array and
# one element from the second array.
# 
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest
# sums.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 10^4
# k <= nums1.length * nums2.length
# 
# 
#
from typing import List
# @lc code=start
import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        heap = []
        result = []

        # initialize heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and k > 0:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return result

    
    
    
    
    
# @lc code=end

