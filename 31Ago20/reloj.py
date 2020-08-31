def relojDigital():
    min = 0
    while(min < 60):
        seg = 0
        while (seg < 60):
            print(f"{min}:{seg}")
            seg += 1
        min += 1
