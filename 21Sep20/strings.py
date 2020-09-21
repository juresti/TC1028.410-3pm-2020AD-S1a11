res = input("Quieres continuar? (si/no) ")
res = res.lower()
while(res == "si"):
    nombre = input("Dime un nombre: ")
    print(f"Me dijiste {nombre}")
    res = input("Quieres continuar? (si/no) ")
    res = res.lower()
    