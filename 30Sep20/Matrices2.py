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

def tamanoMatriz(matriz):
    if(matriz == []):
        return 0,0 #(0,0)
    else:
        numRen = len(matriz)
        numCol = len(matriz[0])#primer renglon
        for renglon in matriz:
            nCol = len(renglon)
            if(numCol != nCol):
                print("Error: matriz mal formada")
                return -1,-1 #Código de error
        return numRen,numCol
    
def esCuadradaV2(matriz):
    numRen,numCol = tamanoMatriz(matriz)
    if(numRen == -1):
        print("Error: matriz mal formada")
        return False
    elif(numRen == numCol):
        return True

def mismoTamano(mat1,mat2):
    numRen1,numCol1 = tamanoMatriz(mat1)
    numRen2,numCol2 = tamanoMatriz(mat2)
    if(numRen1 == -1) or (numRen2 == -1): #codigo error
        print("Error: matrices mal formadas")
        return -1 #código de error
    else:
        if(numRen1 == numRen2):
            if(numCol1 == numCol2):
                return True
            else:
                print("Diferente numero de columnas")
                return False
        else:
            print("Diferente numero de renglones")
            return False

def restarMatrices(mat1,mat2):
    if(mismoTamano(mat1,mat2)):
        numRen,numCol = tamanoMatriz(mat1)
        matResta = crearMatriz(numRen,numCol,0)
        for ren in range(numRen):
            for col in range(numCol):
                matResta[ren][col] = mat1[ren][col] - mat2[ren][col]
        return matResta
    else:
        print("Matrices no son del mismo tamaño")
        return []