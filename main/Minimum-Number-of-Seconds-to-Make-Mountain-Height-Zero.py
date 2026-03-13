1import math
2from typing import List
3
4class Solution:
5    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
6        def can_reduce_in_time(time: int) -> bool:
7            total = 0
8            for wt in workerTimes:
9                if time < wt:
10                    continue
11                # Quadratic formula: max x where wt * x * (x+1) / 2 <= time
12                x = int((-1 + math.sqrt(1 + 8 * time / wt)) / 2)
13                
14                # Adjust for floating-point precision (at most ±1)
15                if wt * (x + 1) * (x + 2) <= 2 * time:
16                    x += 1
17                elif wt * x * (x + 1) > 2 * time:
18                    x -= 1
19                
20                total += max(0, x)
21                if total >= mountainHeight:  # Early exit
22                    return True
23            return False
24        
25        # Binary search on answer
26        # Upper bound: fastest worker does all work alone
27        min_wt = min(workerTimes)
28        lo, hi = 0, min_wt * mountainHeight * (mountainHeight + 1) // 2
29        
30        while lo < hi:
31            mid = (lo + hi) // 2
32            if can_reduce_in_time(mid):
33                hi = mid
34            else:
35                lo = mid + 1
36        
37        return lo