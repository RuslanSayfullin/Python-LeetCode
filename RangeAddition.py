# Дано целое число length и массив updates, где updates[i] = [startIdxi, endIdxi, inci].
# У вас есть массив arr длины length, заполненный нулями. Вам нужно применить некоторые операции к arr. В i-й операции следует увеличить все элементы arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] на inci.
# Верните arr после применения всех обновлений.

"""
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
"""

def getModifiedArray(length, updates):
    result = [0] * length

    for update in updates:
        start, end, val = update
        result[start] += val
        if end + 1 < length:
            result[end+1] -= val

    for i in range(1, length):
        result[i] += result[i - 1]

    return result 

if __name__ == "__main__":
    res = getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]])
    print(res)