# Дано целое число n, посчитайте общее количество единиц, встречающихся во всех неотрицательных числах, меньших или равных n.

"""
Input: n = 13
Output: 6
"""

def countDigitOne(n: int) -> int:
    counter = 0
    i = 1
    while i <= n:
        divider = i * 10
        counter += (n // divider) * i + min(max(n % divider - i +1, 0), i)
        i *= 10
    return counter



if __name__ == "__main__":
    res = countDigitOne(n = 13)
    print(res)
