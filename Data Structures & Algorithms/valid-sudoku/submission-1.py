class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        visitadosCuadros = {}

        for i in range(9):

            visitadosFilas =set()
            visitadosColumns = set()
            for j in range(9):
                cuadro = (i//3,j//3)
                numero  = board[i][j]
                if cuadro not in visitadosCuadros:
                    visitadosCuadros[cuadro] = set()
                    
                if numero !=".":

                    if numero in visitadosCuadros[cuadro]:
                        return False
                    else:
                        visitadosCuadros[cuadro].add(numero)
                numeroFila = board[i][j]
                numeroColumns = board[j][i]
                if numeroFila != ".":
                    if numeroFila in visitadosFilas:
                        return False
                    else:
                        visitadosFilas.add(numeroFila)
                if numeroColumns !=".":
                    if numeroColumns in visitadosColumns:
                        return False
                    else:
                        visitadosColumns.add(numeroColumns)    
        return True        
        