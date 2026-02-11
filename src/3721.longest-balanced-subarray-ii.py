#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#
# https://leetcode.com/problems/longest-balanced-subarray-ii/description/
#
# algorithms
# Hard (11.96%)
# Likes:    156
# Dislikes: 34
# Total Accepted:    17.9K
# Total Submissions: 66.8K
# Testcase Example:  '[2,5,4,3]'

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
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
#
from typing import List

class Node:
    def __init__(self, x=None):
        if x is None:
            self.min = float('inf')
            self.max = float('-inf')
        else:
            self.min = x
            self.max = x
        self.lazy = 0

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        # 1-indexed segment tree with size 4*n
        self.segTree = [Node() for _ in range(self.n * 4)]
        self.build_tree(1, 0, self.n - 1, arr)
    
    def pull(self, i):
        """Pull values from children up to parent"""
        self.segTree[i].min = min(self.segTree[2*i].min, self.segTree[2*i+1].min)
        self.segTree[i].max = max(self.segTree[2*i].max, self.segTree[2*i+1].max)
    
    def build_tree(self, i, l, r, arr):
        if l == r:
            self.segTree[i] = Node(arr[l])
            return
        
        m = (l + r) >> 1
        self.build_tree(2*i, l, m, arr)
        self.build_tree(2*i+1, m+1, r, arr)
        self.pull(i)
    
    def apply(self, i, l, r):
        """Apply lazy propagation"""
        if self.segTree[i].lazy == 0:
            return
        
        self.segTree[i].min += self.segTree[i].lazy
        self.segTree[i].max += self.segTree[i].lazy
        
        if l < r:
            self.segTree[2*i].lazy += self.segTree[i].lazy
            self.segTree[2*i+1].lazy += self.segTree[i].lazy
        
        self.segTree[i].lazy = 0
    
    def update_range(self, start, end, i, l, r, val):
        """Range update with lazy propagation"""
        self.apply(i, l, r)
        
        if l > end or r < start:
            return
        
        if l >= start and r <= end:
            self.segTree[i].lazy += val
            self.apply(i, l, r)
            return
        
        m = (l + r) >> 1
        self.update_range(start, end, 2*i, l, m, val)
        self.update_range(start, end, 2*i+1, m+1, r, val)
        self.pull(i)
    
    def find_last_0(self, i, l, r):
        """Find the last index where value is 0"""
        self.apply(i, l, r)
        
        # If 0 isn't within [min, max], no 0 exists
        if self.segTree[i].min > 0 or self.segTree[i].max < 0:
            return -1
        
        if l == r:
            return l
        
        m = (l + r) >> 1
        # Search right child first to find the last 0
        right = self.find_last_0(2*i+1, m+1, r)
        if right != -1:
            return right
        return self.find_last_0(2*i, l, m)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        
        # For small inputs, use simpler O(n²) approach
        if n <= 2000:
            return self.longestBalanced_simple(nums)
        
        # Find maximum value to size the last array
        M = max(nums)
        last = [n] * (M + 1)
        next_pos = [n] * n
        
        # Build next_pos array (next occurrence of same number)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            next_pos[i] = last[x]
            last[x] = i
        
        # Compute prefix sums based on distinct odd/even counts
        seen = set()
        prefix = []
        sum_val = 0
        
        for i in range(n):
            x = nums[i]
            if x not in seen:
                # Odd numbers: +1, Even numbers: -1
                sum_val += 1 if (x & 1) else -1
                seen.add(x)
            prefix.append(sum_val)
        
        # Build segment tree
        seg = SegmentTree(prefix)
        
        # Initial answer: longest prefix with sum 0
        ans = seg.find_last_0(1, 0, n - 1) + 1
        
        # Process each position
        for i in range(n - 1):
            r = next_pos[i] - 1
            
            # Update range when removing nums[i] from consideration
            if i + 1 <= r:
                # Reverse the contribution of nums[i]
                val = -1 if (nums[i] & 1) else 1
                seg.update_range(i + 1, r, 1, 0, n - 1, val)
            
            # Only search if better answer is possible
            if i + ans + 1 < n:
                right = seg.find_last_0(1, 0, n - 1)
                if right != -1:
                    ans = max(ans, right - i)
        
        return ans
    
    def longestBalanced_simple(self, nums: List[int]) -> int:
        """Simple O(n²) solution for small inputs"""
        n = len(nums)
        max_len = 0
        
        for l in range(n):
            if l > n - max_len:
                break
            
            seen = set()
            diff = 0
            
            for r in range(l, n):
                x = nums[r]
                if x not in seen:
                    # Odd: +1, Even: -1
                    diff += 1 if (x & 1) else -1
                    seen.add(x)
                
                if diff == 0:
                    max_len = max(max_len, r - l + 1)
        
        return max_len

# @lc code=end

