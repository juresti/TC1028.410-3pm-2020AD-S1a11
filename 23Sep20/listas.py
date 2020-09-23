def personas(numPer):
    salida = []
    for cont in range(numPer):
        nombre = input(f"{cont+1}. Dime el nombre: ")
        salida.append(nombre)
    return salida

def personas2(numPer):
    salida = [""] * numPer
    for pos in range(numPer):
        salida[pos] = input(f"{pos+1}. Dime el nombre: ")
    return salida

def imprimePersonas(listaP):
    for persona in listaP:
        print(persona)
        