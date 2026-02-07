#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/
#
# algorithms
# Medium (65.60%)
# Likes:    2376
# Dislikes: 75
# Total Accepted:    220.3K
# Total Submissions: 331.3K
# Testcase Example:  '"aababbab"'

# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# 
# You can delete any number of characters in s to make s balanced. s is
# balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b'
# and s[j]= 'a'.
# 
# Return the minimum number of deletions needed to make s balanced.
# 
# 
# Example 1:
# 
# 
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" ->
# "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" ->
# "aabbbb").
# 
# 
# Example 2:
# 
# 
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is 'a' or 'b'​​.
# 
# 
#


# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        s = s.replace("a", "0").replace("b", "1")
        count_0 = s.count("0")
        count_1 = 0
        result = count_0
        for c in s:
            if c == "0":
                count_0 -= 1
            else:
                count_1 += 1
            result = min(result, count_0 + count_1)
        return result
# @lc code=end

