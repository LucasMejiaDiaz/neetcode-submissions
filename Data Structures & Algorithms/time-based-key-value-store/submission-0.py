class TimeMap:

    def __init__(self):
        self.datos = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.datos:
            self.datos[key] = []
        self.datos[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.datos:
            return ""
        his = self.datos[key]
        izq = 0
        der = len(his) -1
        resultado = ""
        
        while izq <= der :
            mid = (izq+der) //2
            if his[mid][0] <= timestamp :
                resultado = his[mid][1]
                izq = mid +1
            else:
                der = mid -1
        return resultado
        
