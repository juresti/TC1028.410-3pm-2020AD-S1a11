X = int(input("Dime el primer numero: "))
Y = int(input("Dime el segundo numero: "))
Z = int(input("Dime el tercer numero: "))

if ((X > 0) and (Y > 0) and (Z > 0)):
    if((X+Y > Z) and (X+Z > Y) and (Y+Z > X)):
        if (X == Y == Z):
            print("Triangulo equilatero")
        elif (X != Y != Z):
            print("Triangulo escaleno")
        else:
            print("Triangulo isósceles")
    else:
        print("Error en las sumas")
else:
    print("Deben de ser los 3 mayores a cero")