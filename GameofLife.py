# Игра Жизнь, также известная просто как Жизнь, — это клеточный автомат, созданный британским математиком Джоном Хортоном Конуэем в 1970 году.

"""
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [0, 1, -1]
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for i in range(3):
                    for j in range(3):
                        if not (neighbors[i] == 0 and neighbors[j] == 0):
                            r = row + neighbors[i]
                            c = col + neighbors[j]
                            if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                                live_neighbors += 1

                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                board[row][col] = 1 if board[row][col] > 0 else 0

        return board

if __name__ == "__main__":
    example = Solution()
    res = example.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
    print(res)