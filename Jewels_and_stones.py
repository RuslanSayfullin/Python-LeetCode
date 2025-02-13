"""
Вам даны строки jewels, представляющие типы камней, которые являются драгоценностями, и stones, представляющие камни, которые у вас есть. 
Каждый символ в stones является типом камня, который у вас есть. 
Вы хотите узнать, сколько из камней, которые у вас есть, также являются драгоценностями.
Буквы чувствительны к регистру, поэтому "a" считается другим типом камня, чем "A".
"""

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for s in S:
            for j in J:
                if j == s:
                    ans += 1
                    break
        return ans

if __name__ == "__main__":
    example = Solution()
    res = example.numJewelsInStones(J = "aA", S = "aAAbbbb")
    print(res)