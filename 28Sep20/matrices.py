def crearMatriz(numRen,numCol,valor):
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon.append(valor)
            #print(f"Renglon al momento: {renglon}")
        matriz.append(renglon)
        #print(f"Matriz al momento: {matriz}")
    return matriz

import random
def crearMatrizAleatorios(numRen,numCol):
    """Crea una matriz con valores aleatorios entre 0 y 9
    Recibe el numero de renglones y columnas de la matriz"""
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            valor = random.randint(0,9)
            renglon.append(valor)
            #print(f"Renglon al momento: {renglon}")
        matriz.append(renglon)
        #print(f"Matriz al momento: {matriz}")
    return matriz

def pideDatosMatriz(numRen,numCol):
    """Crea una matriz con el número de renglones y columnas
    dadas por el usuario. Va pidiendo los datos de cada posición."""
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            valor = int(input(f"Dime el valor de ({ren+1},{col+1}): "))
            renglon.append(valor)
            #print(f"Renglon al momento: {renglon}")
        matriz.append(renglon)
        #print(f"Matriz al momento: {matriz}")
    return matriz

def imprimirMatriz(matriz):
    strMat = ""
    for renglon in matriz:
        strRen = ""
        for valor in renglon:
            strRen += str(valor) + " "
            #print(f"Renglon al momento: {strRen}")
        strMat += strRen + "\n"
        #print(f"Matriz al momento: {strMat}")
    print(strMat)
    #return strMat