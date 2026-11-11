class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        izq=0
        
        filas = len(matrix)
        columnas = len(matrix[0])
        der= filas * columnas -1

        while izq <= der:
            mid =(izq+der)//2
            fila = mid //columnas
            columna = mid % columnas
            if matrix[fila][columna] == target:
                return True
            elif matrix[fila][columna] < target:
                izq = mid+1
            else:
                der = mid-1
        return False
                

        