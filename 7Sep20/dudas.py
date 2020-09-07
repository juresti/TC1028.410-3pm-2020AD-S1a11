def primo(num):
    for div in range(2,num):
        res = num % div
        if (res == 0):
            return False
    return True

def primos(num):
    for cont in range(1,num + 1):
        if (primo(cont)):
            ultPrimo = cont
            print(cont)
    return ultPrimo

def escalera(hasta):
    salida = ""
    for cont in range(1,hasta + 1):
        salida += str(cont) + ","
     
    cont = hasta - 1
    while(cont > 1):
        salida += str(cont) + ","
        cont -= 1
        
    return salida + "1"
            
            