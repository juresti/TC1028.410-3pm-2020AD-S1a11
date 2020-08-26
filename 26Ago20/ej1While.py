def pares(a,b):
    while(a <= b):
        res = a % 2
        if (res == 0): #es par?
            print(a)
        
        a += 1

def main():
    inf = int(input("Dime limite inferior: "))
    sup = int(input("Dime limite superior: "))
    pares(inf,sup)
    print("\nTerminado")
    
main()
        