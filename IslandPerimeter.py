"""
Дан массив размером row x col, представляющий карту, где grid[i][j] = 1 обозначает сушу, а grid[i][j] = 0 обозначает воду.
Клетки сетки соединены горизонтально/вертикально (не по диагонали). Сетка полностью окружена водой, и на ней находится ровно один остров (т.е. одна или более соединённых ячеек суши).
У острова нет "озёр", то есть вода внутри не соединена с водой вокруг острова. Одна ячейка - это квадрат со стороной 1. 
Сетка прямоугольная, ширина и высота не превышают 100. Определите периметр острова.
"""

"""
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
"""

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    up = 0 if r == 0 else grid[r-1][c]
                    left = 0 if c == 0 else grid[r][c-1]
                    down = 0 if r == rows-1 else grid[r+1][c]
                    right = 0 if c == cols-1 else grid[r][c+1]
                    
                    result += 4 - (up + left + right + down)
        
        return result

if __name__ == "__main__":
    example = Solution()
    res = example.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    print(res)