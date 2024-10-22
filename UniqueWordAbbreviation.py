# Сокращение слова — это объединение его первой буквы, количества символов между первой и последней буквой и последней буквы. Если слово состоит только из двух символов, то оно является сокращением само по себе.

"""
Input
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
Output
[null, false, true, false, true, true]
"""

from typing import List

class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        """
        Создайте словарь сокращений abbrDict, который будет хранить сокращения слов в виде ключей и булевы значения, указывающие, уникально ли сокращение.
        Создайте множество dict, содержащее все слова из словаря, чтобы быстро проверять наличие слова в словаре.
        """
        self.abbr_dict = {}
        self.dict = set(dictionary)
        for word in self.dict:
            abbr = self.to_abbr(word)
            self.abbr_dict[abbr] = not self.abbr_dict.get(abbr, False)

    def ValidWordAbbr(self, word: str) -> bool:
        """
        Для метода isUnique создайте сокращение для входного слова и проверьте, есть ли это сокращение в abbrDict.
        Если сокращение отсутствует в abbrDict, возвращайте true.
        Если сокращение присутствует и оно уникально, проверьте, есть ли это слово в словаре. Если да, возвращайте true, в противном случае - false.
        """
        abbr = self.to_abbr(word)
        has_abbr = self.abbr_dict.get(abbr)
        return has_abbr is None or (has_abbr and word in self.dict)

    def to_abbr(self, word: str) -> str:
        n = len(word)
        if n <= 2:
            return word
        return f"{word[0]}{n - 2}{word[-1]}"

if __name__ == "__main__":
    example = ValidWordAbbr(["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]])
    res = example.ValidWordAbbr()
    print(res)

    
        