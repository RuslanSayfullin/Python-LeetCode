# Вам дана строка currentState, которая содержит только символы '+' и '-'. 
# Вы и ваш друг по очереди переворачиваете две последовательные "++" в "--". 
# Игра заканчивается, когда игрок больше не может сделать ход, и, следовательно, другой игрок становится победителем.
# Верните true, если начальный игрок может гарантировать победу, и false в противном случае.

"""
Input: currentState = "++++"
Output: true
"""

class Solution:
    def canWin(self, currentState: str) -> bool:
        stateArray = list(currentState)
        
        for i in range(len(stateArray) - 1):
            if stateArray[i] == '+' and stateArray[i + 1] == '+':
                stateArray[i] = '-'
                stateArray[i + 1] = '-'
                newState = ''.join(stateArray)
                
                if not self.canWin(newState):
                    stateArray[i] = '+'
                    stateArray[i + 1] = '+'
                    return True
                
                stateArray[i] = '+'
                stateArray[i + 1] = '+'
        
        return False


if __name__ == "__main__":
    example = Solution()
    res = example.canWin(currentState = "++++")
    print(res)
