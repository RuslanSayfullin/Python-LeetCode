# Вам дан отсортированный массив уникальных целых чисел nums.
# Диапазон [a,b] - это множество всех целых чисел от a до b (включительно).
# Верните наименьший отсортированный список диапазонов, которые покрывают все числа в массиве точно. 

"""
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
"""

from typing import List

class Solution:
    def summaryRanges(delf, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start != nums[i]:
                ranges.append(f"{start}->{nums[i]}")
            else:
                ranges.append(f"{start}")
            i += 1
        return ranges

if __name__ == "__main__":
    example = Solution()
    res = example.summaryRanges(nums = [0,1,2,4,5,7])
    print(res)