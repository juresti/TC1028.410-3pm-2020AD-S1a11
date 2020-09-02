def linea(ancho):
    strLin = "" #string vacio
    for cont in range(ancho):
        #print("*")
        strLin += "*" #concatenando
    #print(strLin)
    return strLin

def main():
    wide = int(input("Ancho de la linea: "))
    line = linea(wide)
    print(line)