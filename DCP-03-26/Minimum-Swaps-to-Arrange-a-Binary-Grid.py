1class Solution:
2    def minSwaps(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        # Count the number of trailing zeros in each row
5        trailing_zeros = []
6        for row in grid:
7            count = 0
8            for j in range(n - 1, -1, -1):
9                if row[j] == 0:
10                    count += 1
11                else:
12                    break
13            trailing_zeros.append(count)
14
15        swaps = 0
16        for i in range(n):
17            required_zeros = n - 1 - i
18            found = False
19            for j in range(i, n):
20                if trailing_zeros[j] >= required_zeros:
21                    found = True
22                    # Swap the rows in the trailing_zeros list
23                    while j > i:
24                        trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
25                        j -= 1
26                        swaps += 1
27                    break
28            
29            if not found:
30                return -1
31        
32        return swaps