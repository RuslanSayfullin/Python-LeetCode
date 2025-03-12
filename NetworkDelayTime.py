"""
Дана сеть из узлов, помеченных от 1 до n. 
Также дано times - список времен прохождения сигнала в виде направленных ребер times[i] = (ui, vi, wi), где ui - исходный узел, 
vi - целевой узел, а wi - время прохождения сигнала от источника до цели. Мы пошлем сигнал из заданного узла k. 
Верните минимальное время, которое потребуется всем узлам, чтобы получить сигнал. Если все узлы не могут получить сигнал, верните -1.
"""

# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

import heapq

def networkDelayTime(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    min_heap = [(0, k)]
    min_time = {i: float('inf') for i in range(1, n + 1)}
    min_time[k] = 0

    while min_heap:
        time, node = heapq.heappop(min_heap)
        for neighbor, t in graph[node]:
            new_time = time + t
            if new_time < min_time[neighbor]:
                min_time[neighbor] = new_time
                heapq.heappush(min_heap, (new_time, neighbor))

    max_time = max(min_time.values())
    return max_time if max_time < float('inf') else -1

if __name__ == "__main__":
    example = networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
    print(example)