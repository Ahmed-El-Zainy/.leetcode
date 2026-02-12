#
# @lc app=leetcode id=3713 lang=python3
#
# [3713] Longest Balanced Substring I
#
# https://leetcode.com/problems/longest-balanced-substring-i/description/
#
# algorithms
# Medium (52.46%)
# Likes:    242
# Dislikes: 19
# Total Accepted:    67K
# Total Submissions: 104.8K
# Testcase Example:  '"abbac"'
#
# You are given a string s consisting of lowercase English letters.
# 
# A substring of s is called balanced if all distinct characters in the
# substring appear the same number of times.
# 
# Return the length of the longest balanced substring of s.
# 
# 
# Example 1:
# 
# 
# Input: s = "abbac"
#
# Output: 4

# Explanation:
# 
# The longest balanced substring is "abba" because both distinct characters 'a'
# and 'b' each appear exactly 2 times.
# 
# 
# Example 2:
# 
# Input: s = "zzabccy"
# 
# Output: 4https://huggingface.co/docs/inference-providers/providers/hf-inference
# 
# Explanation:
# 
# The longest balanced substring is "zabc" because the distinct characters 'z',
# 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​
# 
# 
# Example 3:
# 
# 
# Input: s = "aba"
# 
# Output: 2
# 
# Explanation:
# 
# ​​​​​​​One of the longest balanced substrings is "ab" because both distinct
# characters 'a' and 'b' each appear exactly 1 time. Another longest balanced
# substring is "ba".
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

# @lc code=start
class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        convert to list 
        then how can we track long distinct substring ?
        
        
        """
        n = len(s)
        max_len = 0
        for i in range(n):
            freq = [0] * 26
            max_freq = 0
            distinct = 0
            for j in range(i, n):
                idx = ord(s[j]) - ord("a")
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])
                
                length = j - i + 1
                ## balanced condition 
                if max_freq * distinct == length:
                    max_len = max(max_len , length)
        return max_len
# @lc code=end

