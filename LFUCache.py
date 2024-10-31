# Спроектируйте и реализуйте структуру данных для кеша с наименьшим количеством использования (Least Frequently Used, LFU).
# Функции должны иметь среднюю временную сложность O(1).

"""
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]
"""

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minf = 0
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)

    def insert(self, key: int, frequency: int, value: int):
        # Вставить пару частота-значение в cache с заданным ключом.
        self.frequencies[frequency][key] = value
        self.cache[key] = (frequency, self.frequencies[frequency])

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        frequeny. freq_map = self.cache[key]
        value = freg_map.pop(key)
        if not freq_map:
            del self.frequencies[frequency]
            if self.minf == frequency: self.minf += 1
        self.insert(key, frequency + 1, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: return
        if key in self.cache:
            self.cache[key][1][key] = value
            self.get(key)
            return
        if len(self.cache) == self.capacity:
            del_key, _ = self.frequencies[self.minf].popitem(last=False)
            del self.cache[del_key]
        self.minf = 1
        self.insert(key, 1, value)

if __name__ == "__main__":
    example = LFUCache()
    res = example.put(["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]])
    print(res)    
