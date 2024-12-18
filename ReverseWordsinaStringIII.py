# Дана строка s. Необходимо изменить порядок символов в каждом слове в предложении, сохранив при этом пробелы и начальный порядок слов.

"""
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        lastSpaceIndex = -1
        length = len(s)
        
        for strIndex in range(length + 1):
            if strIndex == length or s[strIndex] == ' ':
                startIndex = lastSpaceIndex + 1
                endIndex = strIndex - 1
                while startIndex < endIndex:
                    s[startIndex], s[endIndex] = s[endIndex], s[startIndex]
                    startIndex += 1
                    endIndex -= 1
                lastSpaceIndex = strIndex
        
        return ''.join(s)

if __name__ == "__main__":
    example = Solution()
    res = example.reverseWords(s = "Let's take LeetCode contest")
    print(res)