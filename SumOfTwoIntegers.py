# Даны два целых числа a и b. Вернуть сумму этих двух чисел, не используя операторы + и -..

"""
Input: a = 1, b = 2
Output: 3
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            while y:
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign

if __name__ == "__main__":
    example = Solution()
    res = example.getSum(a=1, b=3)
    print(res)
