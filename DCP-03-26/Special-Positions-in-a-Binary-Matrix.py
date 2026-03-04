1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        m, n = len(mat), len(mat[0])
4        row_sum = [0] * m
5        col_sum = [0] * n
6        for i in range(m):
7            for j in range(n):
8                row_sum[i] += mat[i][j]
9                col_sum[j] += mat[i][j]
10        count = 0
11        for i in range(m):
12            for j in range(n):
13                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
14                    count += 1
15        return count