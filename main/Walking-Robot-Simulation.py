1class Solution:
2    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
3        x = y = 0
4        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
5        direction = 0
6        max_dist = 0
7        obstacle_set = set(map(tuple, obstacles))
8        for command in commands:
9            if command == -2:
10                direction = (direction - 1) % 4
11            elif command == -1:
12                direction = (direction + 1) % 4
13            else:
14                dx, dy = directions[direction]
15                for _ in range(command):
16                    if (x + dx, y + dy) not in obstacle_set:
17                        x += dx
18                        y += dy
19                        max_dist = max(max_dist, x * x + y * y)
20                    else:
21                        break
22        return max_dist
23
24