from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        cola = deque()
        resultado = []

        if root is None:
            return resultado
        
        cola.append(root)

        while cola:
            nivelActual = []
            cantidad = len(cola)

            for i in range(cantidad):
                nodoActual = cola.popleft()
                nivelActual.append(nodoActual.val)

                if nodoActual.left:
                    cola.append(nodoActual.left)
                if nodoActual.right:
                    cola.append(nodoActual.right)
            resultado.append(nivelActual)
        return resultado
