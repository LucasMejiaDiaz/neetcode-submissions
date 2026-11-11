# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visitados = []
        actual = head


        while actual is not None:
            if actual in visitados:
                return True
            else:
                visitados.append(actual)
                actual = actual.next
        return False


        