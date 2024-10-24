# Дана строка s, представляющая выражение. Вычислите это выражение и верните его значение.
# Целочисленное деление должно округляться к нулю.

"""
Input: s = "3+2*2"
Output: 7
"""

class Solution:
    def calculate(self, s: str) -> int:
        length = len(s)
        # Вместо использования стека, используем переменную lastNumber для отслеживания значения последнего вычисленного выражения.
        if length == 0:
            return 0
        currentNumber = 0
        lastNumber = 0
        result = 0
        sign = '+'

        for i in range(length):
            currentChar = s[i]
            if currentChar.isdigit():
                currentNumber = (currentNumber * 10) + int(currentChar)
            if not currentChar.isdigit() and not currentChar.isspace() or i == length -1:
                if sign == '+' or sign == '-':
                    result += lastNumber
                    lastNumber = currentNumber if sign == '+' else -currentNumber
                elif sign == '*':
                    lastNumber *= currentNumber
                elif sign == '/':
                    lastNumber //= currentNumber
                sign = currentChar
                currentNumber = 0
        result += lastNumber
        return result



if __name__ == "__main__":
    example = Solution()
    res = example.calculate(s = "3+2*2")
    print(res)