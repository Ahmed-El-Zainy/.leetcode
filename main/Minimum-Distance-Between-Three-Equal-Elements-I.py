1"""
23740. Minimum Distance Between Three Equal Elements I
3Easy
4Topics
5premium lock icon
6Companies
7Hint
8You are given an integer array nums.
9
10A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
11
12The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
13
14Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
15
16 
17
18Example 1:
19
20Input: nums = [1,2,1,1,3]
21
22Output: 6
23
24Explanation:
25
26The minimum distance is achieved by the good tuple (0, 2, 3).
27
28(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.
29
30Example 2:
31    
32Input: nums = [1,1,2,3,2,1,2]
33
34Output: 8
35
36Explanation:
37
38The minimum distance is achieved by the good tuple (2, 4, 6).
39
40(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.
41
42Example 3:
43
44Input: nums = [1]
45
46Output: -1
47
48Explanation:
49
50There are no good tuples. Therefore, the answer is -1.
51
52"""
53
54from collections import defaultdict
55from typing import List
56
57class Solution:
58    def minimumDistance(self, nums: List[int]) -> int:
59        index_map = defaultdict(list)
60        
61        # Step 1: group indices
62        for i, num in enumerate(nums):
63            index_map[num].append(i)
64        
65        ans = float('inf')
66        
67        # Step 2: process each value
68        for indices in index_map.values():
69            if len(indices) < 3:
70                continue
71            
72            # Step 3: check consecutive triples
73            for i in range(len(indices) - 2):
74                left = indices[i]
75                right = indices[i + 2]
76                ans = min(ans, 2 * (right - left))
77        
78        return ans if ans != float('inf') else -1
79
80
81# if __name__=="__main__":
82
83#     nums = [1]
84#     output = -1
85#     sol = Solution()
86#     print(f"output:{output}, code_output: {sol.minimumDistance(nums)}
87
88
89