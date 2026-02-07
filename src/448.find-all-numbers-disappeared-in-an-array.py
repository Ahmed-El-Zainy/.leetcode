#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n + 1)   # one array (values 0–100)
        # count frequency
        for num in nums:
            freq[num] += 1
        res = []
        for i in range(1, n + 1):
            if freq[i] == 0:
                res.append(i)
        return res
    
# @lc code=end

