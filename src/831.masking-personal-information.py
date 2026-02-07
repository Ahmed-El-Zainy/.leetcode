#
# @lc app=leetcode id=831 lang=python3
#
# [831] Masking Personal Information
#

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            return name[0] + "*****" + name[-1] + "@" + domain
        else:
            digits = [digit for digit in s if digit.isdigit()]
            total_length = len(digits)
            local = "".join(digits[-4:])
            country_len = total_length - 10
            if country_len==0:
                return "***-***-" + local
            else: 
                return "+" + "*" * country_len + "-***-***-" + local

            
# @lc code=end

