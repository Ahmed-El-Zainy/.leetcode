1class Solution:
2    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
3        mod = 10**9 + 7
4        L = limit + 1
5        
6        # dp0[z][o][r]: ways with z zeros, o ones, ending in 0 with run length r
7        dp0 = [[[0] * L for _ in range(one + 1)] for __ in range(zero + 1)]
8        dp1 = [[[0] * L for _ in range(one + 1)] for __ in range(zero + 1)]
9        tot0 = [[0] * (one + 1) for _ in range(zero + 1)]
10        tot1 = [[0] * (one + 1) for _ in range(zero + 1)]
11        
12        # Base cases
13        if zero > 0:
14            dp0[1][0][1] = 1
15            tot0[1][0] = 1
16        if one > 0:
17            dp1[0][1][1] = 1
18            tot1[0][1] = 1
19        
20        for z in range(zero + 1):
21            for o in range(one + 1):
22                if z + o < 2:
23                    continue
24                    
25                if z > 0:
26                    # Start new run of 0s (length 1) from any sequence ending in 1
27                    dp0[z][o][1] = tot1[z-1][o]
28                    # Extend runs: shift dp0[z-1][o][1..limit-1] → dp0[z][o][2..limit]
29                    if limit >= 2:
30                        dp0[z][o][2:L] = dp0[z-1][o][1:limit]
31                    # Total = new run + extended runs
32                    # Sum of extended = tot0[z-1][o] - dp0[z-1][o][limit]
33                    extended = (tot0[z-1][o] - dp0[z-1][o][limit]) % mod
34                    tot0[z][o] = (dp0[z][o][1] + extended) % mod
35                    
36                if o > 0:
37                    # Start new run of 1s (length 1) from any sequence ending in 0
38                    dp1[z][o][1] = tot0[z][o-1]
39                    if limit >= 2:
40                        dp1[z][o][2:L] = dp1[z][o-1][1:limit]
41                    extended = (tot1[z][o-1] - dp1[z][o-1][limit]) % mod
42                    tot1[z][o] = (dp1[z][o][1] + extended) % mod
43        
44        return (tot0[zero][one] + tot1[zero][one]) % mod