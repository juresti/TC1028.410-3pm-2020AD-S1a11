import math

#Ejercicio 1
r = float(input("Dime el radio: "))
area = 4 * math.pi * r ** 2
vol = (4 * math.pi * r ** 3) / 3
print(f"El area es {area:.3f}")
print(f"El volumen del radio {r:.2f} es {vol:.4f}")
