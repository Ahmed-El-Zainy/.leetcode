1from typing import List
2
3class Robot:
4
5    def __init__(self, width: int, height: int):
6        self.w = width
7        self.h = height
8        self.perimeter = 2 * (width + height - 2)
9        self.pos = 0
10        self.moved = False
11        
12    def step(self, num: int) -> None:
13        self.moved = True
14        self.pos = (self.pos + num) % self.perimeter
15        
16    def getPos(self) -> List[int]:
17        if self.pos == 0:
18            return [0, 0]
19            
20        # Bottom edge: positions 1 to w-1 (indices 1 to w-1)
21        if self.pos <= self.w - 1:
22            return [self.pos, 0]
23            
24        # Right edge: positions w to w+h-2 (indices w to w+h-2)
25        elif self.pos <= self.w + self.h - 2:
26            return [self.w - 1, self.pos - (self.w - 1)]
27            
28        # Top edge: positions w+h-1 to 2*w+h-3 (indices w+h-1 to 2*w+h-3)
29        elif self.pos <= 2 * self.w + self.h - 3:
30            return [2 * self.w + self.h - 3 - self.pos, self.h - 1]
31            
32        # Left edge: positions 2*w+h-2 to perimeter-1
33        else:
34            return [0, self.perimeter - self.pos]
35            
36    def getDir(self) -> str:
37        if self.pos == 0:
38            return "East" if not self.moved else "South"
39            
40        if self.pos <= self.w - 1:
41            return "East"
42        elif self.pos <= self.w + self.h - 2:
43            return "North"
44        elif self.pos <= 2 * self.w + self.h - 3:
45            return "West"
46        else:
47            return "South"