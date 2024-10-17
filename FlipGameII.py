# Вы играете в игру Flip со своим другом.
# Вам дана строка currentState, которая содержит только символы '+' и '-'. 
# Вы и ваш друг по очереди переворачиваете две последовательные "++" в "--". 
# Игра заканчивается, когда один из игроков больше не может сделать ход, и, следовательно, другой игрок становится победителем.
# Верните все возможные состояния строки currentState после одного допустимого хода. 
# Вы можете вернуть ответы в любом порядке. Если допустимых ходов нет, верните пустой список [].

"""
Input: currentState = "++++"
Output: ["--++","+--+","++--"]
"""

from typing import List

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        nextPossibleStates = []

        for index in range(len(currentState) - 1):
            if currentState[index] == "+" and currentState[index + 1] == "+":
                nextState = currentState[:index] + "--" + currentState[index + 2:]
                nextPossibleStates.append(nextState)

        return nextPossibleStates

if __name__ == "__main__":
    example = Solution()
    res = example.generatePossibleNextMoves(currentState = "++++")
    print(res)
