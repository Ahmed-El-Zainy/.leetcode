#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (62.74%)
# Likes:    2745
# Dislikes: 199
# Total Accepted:    92.2K
# Total Submissions: 146.6K
# Testcase Example:  '"bcabc"'
#
# Given a string s, return the lexicographically smallest subsequence of s that
# contains all the distinct characters of s exactly once.
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
# 
# Note: This question is the same as 316:
# https://leetcode.com/problems/remove-duplicate-letters/
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # result = list(s)
        # unique_result = sorted(set(result))
        # return ''.join(unique_result)
        
        
        
        result = list(dict.fromkeys(list(s)))

        unique_list = []
        for char in result:
            if char not in unique_list:
                unique_list.append(char)
        result = ''.join(sorted(unique_list))
        return result
    
# @lc code=end

