# Даны два вектора целых чисел v1 и v2, реализуйте итератор, который возвращает их элементы поочередно.
# Реализуйте класс ZigzagIterator:
# ZigzagIterator(List<int> v1, List<int> v2) инициализирует объект с двумя векторами v1 и v2.
# boolean hasNext() возвращает true, если в итераторе еще есть элементы, и false в противном случае.
# int next() возвращает текущий элемент итератора и перемещает итератор к следующему элементу.

"""
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
"""

from collections import deque

class ZigzagIterator:
    """
    Класс ZigzagIterator с двумя списками v1 и v2.
    """
    def __init__(self, v1, v2):
        # Сохраните списки в структуре vectors.
        self.vectors = [v1, v2]
        # Очередь queue, содержащую пары индексов: индекс списка и индекс элемента в этом списке, если список не пуст
        self.queue = deque((i, 0) for i, vec in enumerate(self.vectors) if vec)

    def next(self):
        vecIndex, elemIndex = self.queue.popleft()
        if elemIndex + 1 < len(self.vectors[vecIndex]):
            self.queue.append((vecIndex, elemIndex + 1))
        return self.vectors[vecIndex][elemIndex]

    def hasNext(self):
        # Проверьте, пуста ли очередь.
        return bool(self.queue)

if __name__ == "__main__":
    example = ZigzagIterator( v1 = [1,2], v2 = [3,4,5,6])
    print(example.next())

