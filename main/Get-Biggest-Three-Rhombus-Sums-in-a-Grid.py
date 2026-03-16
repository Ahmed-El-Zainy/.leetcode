1from typing import List
2
3class Solution:
4    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
5        m, n = len(grid), len(grid[0])
6        sums = set()
7        
8        def get_rhombus_sum(i: int, j: int, k: int) -> int:
9            """حساب مجموع حدود معين رأسه العلوي عند (i,j) وطول ضلعه k"""
10            if k == 0:
11                return grid[i][j]
12            
13            # التأكد من أن المعين داخل حدود الشبكة
14            if i + 2*k >= m or j - k < 0 or j + k >= n:
15                return -1
16            
17            total = 0
18            # الضلع الأول: من الأعلى لليمين ↘
19            for d in range(k):
20                total += grid[i + d][j + d]
21            # الضلع الثاني: من اليمين للأسفل ↙
22            for d in range(k):
23                total += grid[i + k + d][j + k - d]
24            # الضلع الثالث: من الأسفل لليسار ↖
25            for d in range(k):
26                total += grid[i + 2*k - d][j - d]
27            # الضلع الرابع: من اليسار للأعلى ↗
28            for d in range(k):
29                total += grid[i + k - d][j - k + d]
30            
31            return total
32        
33        # تجربة كل موضع ممكن كرأس علوي للمعين
34        for i in range(m):
35            for j in range(n):
36                # أقصى حجم للمعين من هذا الموضع
37                max_k = min((m - 1 - i) // 2, j, n - 1 - j)
38                for k in range(max_k + 1):
39                    s = get_rhombus_sum(i, j, k)
40                    if s != -1:
41                        sums.add(s)
42        
43        # إرجاع أكبر 3 قيم مميزة
44        return sorted(sums, reverse=True)[:3]