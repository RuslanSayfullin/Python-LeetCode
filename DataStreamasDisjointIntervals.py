# Дано поступление данных из последовательности неотрицательных целых чисел a1, a2, ..., an, необходимо обобщить увиденные числа в виде списка непересекающихся интервалов.
# Реализуйте класс SummaryRanges:
# SummaryRanges() Инициализирует объект с пустым потоком.
# void addNum(int value) Добавляет целое число в поток.
# int[][] getIntervals() Возвращает обобщение текущих чисел в потоке в виде списка непересекающихся интервалов [starti, endi]. Ответ должен быть отсортирован по starti.

"""
Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
"""

class SummaryRanges:
    def __init__(self):
        # Инициализировать структуру данных TreeSet для хранения значений.
        self.values = set()

    def addNum(self, value: int) -> None:
        self.values.add(value)

    def getIntervals(self) -> list[list[int]]:
        if not self.values:
            return []
        intervals = []
        sorted_values = sorted(self.values)
        left, right = -1, -1
        for value in sorted_values:
            if left < 0:
                left, right = value, value
            elif value == right + 1:
                right = value
            else:
                intervals.append([left, right])
                left, right = value, value
        intervals.append([left, right])
        return intervals


if __name__ == "__main__":
    example = SummaryRanges()
    res = example.addNum([[], [1], [], [3], [], [7], [], [2], [], [6], []])
    print(res)