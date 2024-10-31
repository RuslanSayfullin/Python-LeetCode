# Дан головной элемент односвязного списка. Верните true, если список является палиндромом, и false в противном случае.

"""
Input: head = [1,2,2,1]
Output: true
"""

from listnode import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        currentNode = head

        while currentNode is not None:
            vals.append(currentNode.val)
            currentNode = currentNode.next

        front = 0
        back = len(vals) - 1
        while front < back:
            if vals[front] != vals[back]:
                return False
            front += 1
            back -= 1
        return True

if __name__ == "__main__":
    example = Solution()
    res = example.isPalindrome(head = [1,2,2,1])
    print(res)
