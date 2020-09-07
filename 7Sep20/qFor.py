def sumaDivisibles3y7(hasta):
  suma = 0
  for num in range (1,hasta):
    suma = 0
    print(suma)
    res3 = num % 3
    res7 = num % 7
    if ((res3 == 0) and (res7 == 0)):
      suma += num
    print(suma)
  return suma