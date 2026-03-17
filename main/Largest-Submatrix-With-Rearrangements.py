1from typing import List
2
3class Solution:
4    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
5        """
6        Find the largest submatrix of 1s after optimally rearranging columns.
7        
8        Key insight: Since we can rearrange columns arbitrarily, for each row,
9        we can treat the heights of consecutive 1s as a histogram and sort them
10        to find the maximum rectangle area.
11        
12        Algorithm:
13        1. Compute height of consecutive 1s for each cell (going upward)
14        2. For each row, sort heights in descending order
15        3. For each position j in sorted row: area = height[j] * (j+1)
16           (we can pick j+1 columns with height >= height[j])
17        4. Track maximum area across all rows
18        """
19        m, n = len(matrix), len(matrix[0])
20        
21        # Step 1: Calculate height of consecutive 1s ending at each cell
22        # If matrix[i][j] == 1, accumulate height from row above
23        # If matrix[i][j] == 0, height resets to 0
24        for i in range(1, m):
25            for j in range(n):
26                if matrix[i][j] == 1:
27                    matrix[i][j] += matrix[i-1][j]
28        
29        max_area = 0
30        
31        # Step 2-4: For each row, sort heights and calculate max rectangle area
32        for i in range(m):
33            # Sort current row's heights in descending order
34            # This simulates optimal column rearrangement
35            matrix[i].sort(reverse=True)
36            
37            # Calculate max area for this row as base
38            for j in range(n):
39                # Width = j+1 (number of columns we can use)
40                # Height = matrix[i][j] (minimum height among these columns)
41                area = matrix[i][j] * (j + 1)
42                max_area = max(max_area, area)
43        
44        return max_area