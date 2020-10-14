def limpiaLista(lista):
    """Recibe una lista que contiene strings con \n
    Regresa una lista sin los \n"""
    for pos in range(len(lista)):
        lista[pos] = lista[pos].rstrip()
    return lista

def initMatrizArchivo(nomArch):
    with open(nomArch + ".txt","r") as file:
        datos = file.readlines()
        
    datos = limpiaLista(datos)
    #print(datos)
    numRen = int(datos[0][0])
    numCol = int(datos[0][2])
    #print(numRen,numCol)
    renglones = datos[1:]
    #print(renglones)
    if len(renglones) != numRen:
        print("Error. Numero de renglones mal en el archivo.")
        return []
    else:
        for pos in range(len(renglones)):
            renglones[pos] = renglones[pos].split(",")
        #print(renglones)
        for ren in range(numRen):
            for col in range(numCol):
                renglones[ren][col] = int(renglones[ren][col])
        return renglones