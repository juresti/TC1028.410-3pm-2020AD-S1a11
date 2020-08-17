import math

#Ejercicio 2
a = 1
b = 2
c = 3

s = (a + b + c) / 2
area = math.sqrt(s * (s-a) * (s-b) * (s-c))

print(f"El valor del area es {area:.3f}")
