"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        connection = {}
        current = head
        if head is None:
            return None

        while  current:
            newNodo = Node(current.val)
            connection[current] = newNodo
            current = current.next
        current = head
        while current:
            if current.next is not None:
                connection[current].next = connection[current.next] 
            if current.random is not None:
                connection[current].random = connection[current.random]
            current = current.next
        
        return connection[head]

                


