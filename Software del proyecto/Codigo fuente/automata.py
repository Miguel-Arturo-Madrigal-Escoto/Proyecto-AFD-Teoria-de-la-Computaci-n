class AFD:
    def __init__(self, qn) -> None:
        #estado actual
        self.__estado = qn

        #arreglo de símbolos de entrada
        self.__simbolos = []

        #modelo matricial (tabla de estado siguiente)
        # (x, y) = z, x = estado actual, y = símbolo de entrada, z = estado siguiente
        self.matriz = {
            (0, 1) : 1, (4, 0)  : 10, (9, 2)  : 1,
            (1, 1) : 2, (7, 0)  : 12, (13, 2) : 5,
            (2, 1) : 3, (8, 0)  : 17, (16, 2) : 13,
            (3, 1) : 4, (19, 0) : 22, (18, 2) : 9,
            (4, 1) : 5,               (23, 2) : 15,
            (5, 1) : 6,
            (6, 1) : 7,
            (7, 1) : 8,
            (8, 1) : 9,
            (9, 1) : 10,
            (10, 1) : 11,
            (11, 1) : 12,
            (12, 1) : 13,
            (13, 1) : 14,
            (14, 1) : 15,
            (15, 1) : 16,
            (16, 1) : 17,
            (17, 1) : 18,
            (18, 1) : 19,
            (19, 1) : 20,
            (20, 1) : 21,
            (21, 1) : 22,
            (22, 1) : 23,
            (23, 1) : 24,
            (24, 1) : 24,     
        }
        
    def getEstadoActual(self) -> int:
        return self.__estado

    def setEstadoActual(self, estado) -> None:
        self.__estado = estado
       
    def agregarSimboloEntrada(self, simbolo) -> None:
        self.__simbolos.append(simbolo)

    def getSimboloEntrada(self, i) -> int:
        return self.__simbolos[i]
    
    def getSimbolosEntrada(self) -> list:
        return self.__simbolos