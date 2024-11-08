# Дан массив различных целых чисел nums и целое число target. Верните количество возможных комбинаций, которые в сумме дают target.


"""
Input: nums = [9], target = 3
Output: 0
"""

from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.combs(nums, target)

    def combs(self, nums: List[int], remain: int) -> int:
        if remain == 0:
            return 1
        if remain in self.memo:
            return self.memo[remain]

        result = 0
        for num in nums:
            if remain - num >= 0:
                result += self.combs(nums, remain - num)

        self.memo[remain] = result
        return result

if __name__ == "__main__":
    example = Solution()
    res = example.combinationSum4(nums = [9], target = 3)
    print(res)