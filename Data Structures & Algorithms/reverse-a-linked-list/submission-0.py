# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actual = head
        anterior = None

        while actual is not None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente
        return anterior



        
        