1class Solution:
2    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
3        if rows==1:
4            return encodedText 
5        n = len(encodedText)
6        cols = n // rows
7        matrix = [
8            list(encodedText[i * cols: (i+ 1) * cols])
9            for i in range(rows)
10        ]
11        result = []
12        for start_col in range(cols):
13            r, c = 0, start_col
14            while r < rows and c < cols:
15                result.append(matrix[r][c])
16                r += 1
17                c += 1
18        return "".join(result).rstrip()