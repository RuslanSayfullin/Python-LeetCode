# Мы можем перемешать строку s, чтобы получить строку t, используя следующий алгоритм:
# Дано положительное целое число n. Найдите наименьшее целое число, которое имеет точно такие же цифры, 
# как и число n, и больше самого числа n по значению. Если такого положительного целого числа не существует, верните -1.

"""
Input: n = 12
Output: 21
"""

class Solution:
    def swap(self, s, i0, i1):
        if i0 == i1:
            return s
        s = list(s)
        s[i0], s[i1] = s[i1], s[i0]
        return ''.join(s)
    
    def permute(self, a, l, r):
        if l == r:
            self.list.append(a)
        else:
            for i in range(l, r + 1):
                a = self.swap(a, l, i)
                self.permute(a, l + 1, r)
                a = self.swap(a, l, i)
    
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        self.list = []
        self.permute(s, 0, len(s) - 1)
        self.list.sort()
        if s in self.list:
            index = self.list.index(s)
            if index < len(self.list) - 1:
                result = int(self.list[index + 1])
                if result <= 2**31 - 1:
                    return result
        return -1

if __name__ == "__main__":
    example = Solution()
    res = example.nextGreaterElement(n = 12)
    print(res)