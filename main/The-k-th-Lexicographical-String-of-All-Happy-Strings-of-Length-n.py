1class Solution:
2    def getHappyString(self, n: int, k: int) -> str:
3        def backtrack(path: str):
4            if len(path) == n:
5                result.append(path)
6                return
7            for c in 'abc':
8                if not path or path[-1] != c:
9                    backtrack(path + c)
10
11        result = []
12        backtrack('')
13        return result[k - 1] if k <= len(result) else ''
14