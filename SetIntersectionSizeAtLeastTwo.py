"""
Вам дан двумерный целочисленный массив intervals, в котором intervals[i] = [starti, endi] представляет все целые числа от starti до endi включительно. 
Содержащее множество - это массив nums, в котором каждый интервал из intervals содержит не менее двух целых чисел в nums. 
Например, если intervals = [[1,3], [3,7], [8,9]], то [1,2,4,7,8,9] и [2,3,4,8,9] - содержащие множества. 
Верните минимально возможный размер содержащего множества.
"""

# intervals = [[1,3],[3,7],[8,9]]
# Output: 5

def minSetSize(intervals):
    # Сортируем интервалы по их конечным точкам.
    intervals.sort(key = lambda x: x[1])
    # пустое множество для хранения чисел.
    nums = []

    # Проходим по каждому интервалу, добавляя необходимые числа в множество так, чтобы каждый интервал содержал не менее двух чисел из этого множества.
    for start, end in intervals:
        if not nums or nums[-1] < start:
            nums.append(end - 1)
            nums.append(end)
        elif nums[-1] == (end - 1):
            nums.append(end)
    return len(nums)

if __name__ == "__main__":
    example = minSetSize(intervals = [[1,3],[3,7],[8,9]])
    print(example)
