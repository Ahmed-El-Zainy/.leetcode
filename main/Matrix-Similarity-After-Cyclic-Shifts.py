1class Solution:
2    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
3        """
4        results = []
5        n = len(mat)
6        for I in rang(len(mat)):
7            if k % n ==0 :
8                return True
9                for j in range(i+1):
10                    if i %2 = 0:
11                    
12        """
13        m = len(mat)
14        n = len(mat[0])
15        for i in range(m):
16            if k % n == 0:
17                return  True
18
19            if i %2==0 :
20                for j in range(n):
21                    if mat[i][j] != mat[i][(j + k) % n]:
22                        return False
23
24            else:
25                for j in range(n):
26                    if mat[i][j] != mat[i][(j - k) % n]:
27                        return False
28        return True
29