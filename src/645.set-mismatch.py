#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
from typing import List
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     print(i)
        #     for j in range(i + 1):
        #         if i == j :
        #             return [i, i+1]
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        expected_sum = n * (n + 1) // 2
        print(f"expected_sim: {expected_sum}")
        actual_sum = sum(nums)
        print(f"actual_sum: {actual_sum}")
        actual_set_sum = sum(set(nums))
        print(f"actual_set_sum: {actual_set_sum}")
        duplicate = actual_sum - actual_set_sum
        print(f"duplicate: {duplicate}")
        missing = expected_sum - actual_set_sum
        print(f"missing: {missing}")
        return [duplicate, missing]
    
# @lc code=end

# if __name__=="__main__":
#     # nums = [1, 2, 3, 4, 4, 5, 5]
#     # sol = Solution()
#     # print(f"outputs" {sol.})