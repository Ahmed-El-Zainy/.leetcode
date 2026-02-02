#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/

# algorithms
# Easy (47.06%)
# Likes:    6808
# Dislikes: 563
# Total Accepted:    586.3K
# Total Submissions: 1.2M
# Testcase Example:  '"abab"'
#
# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
# 
# 
# Example 1:
# 
# 
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# 
# 
# Example 2:

# 
# Input: s = "aba"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc"
# twice.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
    
# @lc code=end


