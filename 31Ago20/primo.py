def primo(num):
    cont = num - 1
    while (cont > 1):
        res = num % cont
        if (res == 0):
            return False
        cont -= 1
    return True

def primos(num):
    cont = 1
    while (cont <= num):
        if(primo(cont)):
            #print(cont)
            ultimo = cont
        cont += 1
    return ultimo