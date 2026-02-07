#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#
# https://leetcode.com/problems/license-key-formatting/description/
#
# algorithms
# Easy (45.28%)
# Likes:    1190
# Dislikes: 1460
# Total Accepted:    346.7K
# Total Submissions: 762.2K
# Testcase Example:  '"5F3Z-2e-9-w"\n4'
#
# You are given a license key represented as a string s that consists of only
# alphanumeric characters and dashes. The string is separated into n + 1 groups
# by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k
# characters, except for the first group, which could be shorter than k but
# still must contain at least one character. Furthermore, there must be a dash
# inserted between two groups, and you should convert all lowercase letters to
# uppercase.
# 
# Return the reformatted license key.
# 
# 
# Example 1:
# 
# 
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4
# characters.
# Note that the two extra dashes are not needed and can be removed.
# 
# 
# Example 2:
# 
# 
# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2
# characters except the first part as it could be shorter as mentioned
# above.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of English letters, digits, and dashes '-'.
# 1 <= k <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        groups = [s[i:i+k] for i in range(0, len(s), k)]
        return "-".join(groups)[::-1]
    
# @lc code=end

