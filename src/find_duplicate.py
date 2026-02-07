from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101   # one array (values 0–100)

        # count frequency
        for num in nums:
            freq[num] += 1
        print(f"freq: {freq[:10]}")
        
        # prefix sum
        for i in range(1, 101):
            freq[i] += freq[i - 1]
        print(f"prefix sum: {freq[:15]}")
        # build result
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                print(f"num -1 : {freq[num -1]}")
                result.append(freq[num - 1])

        return result

        
        
        
        
if __name__=="__main__":
    nums = [8,1,2,2,3]
    Output =  [4,0,1,1,3]
    sol = Solution()
    print(f"Correct: {Output},Solution: {sol.smallerNumbersThanCurrent(nums)}")
