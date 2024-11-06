# Дан массив целых чисел nums. Верните true, если существуют такие три индекса (i, j, k), что i < j < k и nums[i] < nums[j] < nums[k]. Если таких индексов не существует, верните false.

"""
Input: nums = [2,1,5,0,4,6]
Output: true
"""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float('inf')
        second_num = float('inf')
        
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False

if __name__ == "__main__":
    example = Solution()
    res = example.increasingTriplet(nums = [2,1,5,0,4,6])
    print(res)