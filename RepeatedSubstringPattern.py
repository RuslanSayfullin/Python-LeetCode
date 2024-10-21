# Дана строка s, проверьте, может ли она быть построена путем взятия подстроки и добавления нескольких копий этой подстроки друг за другом.

"""
Input: heights = [2,1,5,6,2,3]
Output: bool
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s) # Создайте целочисленную переменную n, равную длине строки s.
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True
        return False

if __name__ == "__main__":
    example = Solution()
    res = example.repeatedSubstringPattern( s = [2,1,5,6,2,3])
    print(res)
