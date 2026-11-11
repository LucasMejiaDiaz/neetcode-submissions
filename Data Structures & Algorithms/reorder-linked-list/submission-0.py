# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        actual  = head
        anterior = None
        stack = []
        while actual is not None:
            stack.append(actual)
            actual = actual.next

        actual  = head
        contador = len(stack) //2
        ultimo = stack.pop()
        
        while contador > 0 :
            
            anterior = actual.next
            actual.next = ultimo
            ultimo.next = anterior
            actual = anterior
            contador -=1
            if ultimo is not 0 :
                ultimo = stack.pop()

        actual.next = None




        