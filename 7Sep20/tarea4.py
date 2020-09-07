def linea(ancho):
    strLin = ""
    for cont in range(ancho):
        strLin += "*"
    return strLin

def rect(ancho,alto):
    strRec = ""
    for cont in range(alto):
        strRec += linea(ancho) + "\n"
    return strRec

def lineaEsp(ancho):
    strLin = "*"
    for cont in range(ancho - 2):
        strLin += " "
    strLin += "*"
    return strLin

def rectEsp(ancho,alto):
    rec = linea(ancho) + "\n"
    for cont in range(alto - 2):
        rec += lineaEsp(ancho) + "\n"
    rec += linea(ancho) + "\n"
    return rec

def variosCuadros(ancho,alto,num):
    recs = ""
    for cont in range(num):
        recs += rectEsp(ancho,alto) + "\n"#recs = recs +
    return recs

def generaU(ancho,alto):
    strU = ""
    for cont in range(alto - 1):
        strU += lineaEsp(ancho) + "\n"
    strU += linea(ancho)
    return strU

def cuadrosJuntos(ancho,alto,num):
    cuads = linea(ancho) + "\n"
    for cont in range(num):
        cuads += generaU(ancho,alto - 1) + "\n"
    return cuads

def main():
    #Ejercicio 1
    print("Ejercicio 1 **** \nCuadro solido")
    ancho = int(input("Dime el ancho: "))
    alto = int(input("Dime el alto: "))
    print(rect(ancho,alto))
    
    #Ejercicio 2
    print("Ejercicio 2 **** \nCuadro espacios")
    ancho = int(input("Dime el ancho: "))
    alto = int(input("Dime el alto: "))
    print(rectEsp(ancho,alto))
