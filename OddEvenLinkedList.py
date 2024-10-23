# Дан заголовок односвязного списка. 
# Сгруппируйте все узлы с нечетными индексами вместе, а затем узлы с четными индексами, и верните упорядоченный список.
# Первый узел считается нечетным, второй узел — четным и так далее.
# Учтите, что относительный порядок внутри обеих групп (четной и нечетной) должен оставаться таким же, как в исходном списке.
# Вы должны решить задачу с дополнительной сложностью по памяти O(1) и временной сложностью O(n).

"""
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        odd, even = head, head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return head

if __name__ == "__main__":
    example = Solution()
    res = example.oddEvenList(head = [2,1,3,5,6,4,7])
    print(res)