1# @lc app=leetcode id=3600 lang=python3
2#
3# [3600] Maximize Spanning Tree Stability with Upgrades
4#
5# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/description/  
6#
7
8from typing import List
9
10class Solution:
11    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
12        mandatory_edges = []
13        optional_edges = []
14        
15        for ui, vi, si, musti in edges:
16            if musti == 1:
17                mandatory_edges.append((ui, vi, si))
18            else:
19                optional_edges.append((ui, vi, si))
20        
21        # Union-Find helpers
22        def find(parent, x):
23            if parent[x] != x:
24                parent[x] = find(parent, parent[x])
25            return parent[x]
26        
27        def union(parent, x, y):
28            px, py = find(parent, x), find(parent, y)
29            if px != py:
30                parent[px] = py
31                return True
32            return False
33        
34        def can_form_base_spanning_tree():
35            """Check if mandatory edges form a valid forest (no cycles)"""
36            if len(mandatory_edges) > n - 1:
37                return False
38            parent = list(range(n))
39            for ui, vi, si in mandatory_edges:
40                if not union(parent, ui, vi):
41                    return False
42            return True
43        
44        def can_achieve(stability_target):
45            """Check if stability >= stability_target is achievable with at most k upgrades"""
46            if not can_form_base_spanning_tree():
47                return False
48            
49            parent = list(range(n))
50            edges_count = 0
51            upgrades_used = 0
52            
53            # Add mandatory edges (cannot be upgraded)
54            for ui, vi, si in mandatory_edges:
55                if si < stability_target:
56                    return False
57                if union(parent, ui, vi):
58                    edges_count += 1
59            
60            # Separate optional edges
61            free_edges = []      # Already meet target, no upgrade needed
62            need_upgrade = []     # Need upgrade but reachable with upgrade
63            
64            for ui, vi, si in optional_edges:
65                if si >= stability_target:
66                    free_edges.append((ui, vi))
67                elif 2 * si >= stability_target:
68                    need_upgrade.append((ui, vi, si))
69            
70            # Priority: use free edges first, then upgradable edges (prefer stronger originals)
71            need_upgrade.sort(key=lambda x: x[2], reverse=True)
72            
73            # Use free edges
74            for ui, vi in free_edges:
75                if union(parent, ui, vi):
76                    edges_count += 1
77                    if edges_count == n - 1:
78                        return upgrades_used <= k
79            
80            # Use upgradable edges
81            for ui, vi, si in need_upgrade:
82                if union(parent, ui, vi):
83                    edges_count += 1
84                    upgrades_used += 1
85                    if edges_count == n - 1:
86                        return upgrades_used <= k
87            
88            # Final check: did we connect all nodes?
89            return edges_count == n - 1 and upgrades_used <= k
90        
91        # Quick sanity check
92        if not can_form_base_spanning_tree():
93            return -1
94        
95        # Binary search on possible stability values
96        min_strength = min(si for _, _, si, _ in edges)
97        max_strength = max(2 * si for _, _, si, _ in edges)
98        
99        left, right = min_strength, max_strength
100        best = -1
101        
102        while left <= right:
103            mid = (left + right) // 2
104            if can_achieve(mid):
105                best = mid
106                left = mid + 1
107            else:
108                right = mid - 1
109        
110        return best