# Дополнение целого числа — это число, которое получается при замене всех 0 на 1 и всех 1 на 0 в его двоичном представлении.
# Например, целое число 5 в двоичной системе — "101", и его дополнение — "010", что соответствует целому числу 2. Дано целое число num, верните его дополнение.

"""
Input: num = 5
Output: 2
"""

class Solution:
    def findComplement(self, num: int) -> int:
        bitmask = num
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        return bitmask ^ num

if __name__ == "__main__":
    example = Solution()
    res = example.findComplement(num = 5)
    print(res)