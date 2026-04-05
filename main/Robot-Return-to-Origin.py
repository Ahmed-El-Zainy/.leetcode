1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        self.x, self.y= 0,0
4        for move in moves:
5            if move =="U":
6                self.y += 1
7            elif move=="D":
8                self.y -= 1
9            elif move=="R":
10                self.x += 1
11            elif move=="L":
12                self.x -= 1
13        return self.x ==0 and  self.y ==0