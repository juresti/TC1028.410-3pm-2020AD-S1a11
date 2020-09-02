def preg7():
    for num in range(7): #genera lista [ ]
        edad = int(input("Dime la edad: "))
        print(f"Me dijiste {edad}")
        
def preg7v2():
    for num in (8,"a",False,3.4,1.1,True,"Adios"):#uso tupla ( )
        edad = int(input("Dime la edad: "))
        print(f"Me dijiste {edad}")
        
def preg7v3():
    for num in range(1,8):
        edad = int(input(f"{num}. Dime la edad: "))
        print(f"Me dijiste {edad}")