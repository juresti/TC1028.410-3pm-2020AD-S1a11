def limpiaLista(lista):
    """Recibe una lista que contiene strings con \n
    Regresa una lista sin los \n"""
    for pos in range(len(lista)):
        lista[pos] = lista[pos].rstrip()
    return lista

def consultaArchivo(nomArch):
    with open(nomArch + ".txt","r") as archivo:
        registros = archivo.readlines()
        
    #print(registros)
    registros = limpiaLista(registros)
    #print(registros)
    
    numReg = len(registros) // 3
    pos = 0 #posición en la lista
    for num in range(numReg):
        print(f"DATOS DEL REGISTRO {num + 1}")
        print(f"Nombre: {registros[pos + 0]}")
        print(f"Edad: {registros[pos + 1]}")
        print(f"Estado civil: {registros[pos + 2]}\n")
        pos += 3
        
def consultaUnRegistro(numReg,nomArch):
    with open(nomArch + ".txt","r") as archivo:
        registros = archivo.readlines()
        
    registros = limpiaLista(registros)
    
    pos = (numReg - 1) * 3
    print(f"DATOS DEL REGISTRO {numReg}")
    print(f"Nombre: {registros[pos + 0]}")
    print(f"Edad: {registros[pos + 1]}")
    print(f"Estado civil: {registros[pos + 2]}\n")
    