# Целочисленный массив называется арифметическим, если он состоит не менее чем из трех элементов и если разность между любыми двумя последовательными элементами одинакова. 
# Например, [1,3,5,7,9], [7,7,7] и [3,-1,-5,-9] являются арифметическими последовательностями. 
# Если задан целочисленный массив nums, верните количество арифметических подмассивов массива nums. Подмассив - это непрерывная подпоследовательность массива.

"""
Input: nums = [1,2,3,4]
Output: 3
"""

def numberOfArithmeticSlices(nums):
    count = 0
    current_length = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            current_length += 1
            count += current_length
        else:
            current_length = 0
    return count

if __name__ == "__main__":
    res = numberOfArithmeticSlices(nums = [1,2,3,4])
    print(res)