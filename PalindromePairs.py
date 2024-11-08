# Дан массив уникальных строк words, индексируемый с 0.
# Пара палиндромов — это пара целых чисел (i, j), таких что:
#   0 <= i, j < words.length,
#   i != j, и
#   words[i] + words[j] (конкатенация двух строк) является палиндромом.
# Верните массив всех пар палиндромов из слов.

"""
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
"""

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                combined = words[i] + words[j]
                if combined == combined[::-1]:
                    pairs.append([i, j])
        
        return pairs
        
if __name__ == "__main__":
    example = Solution()
    res = example.palindromePairs(words = ["abcd","dcba","lls","s","sssll"])
    print(res)