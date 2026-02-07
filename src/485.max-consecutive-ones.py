#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in nums: 
            if i ==1 :
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
                
        return max_count
    
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         count = 0
        # return count
    
    
# @lc code=end

if __name__=="__main__":
    sol = Solution()
    nums = [1, 1, 1, 0, 1, 1, 0]
    print(f"output: {sol.findMaxConsecutiveOnes(nums=nums)}, correct answer: 3")