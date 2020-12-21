def dec2bin():
    num = int(input("Decimal Number:"))
    binnum=0
    power=0
    while num > 0:
        binnum += 10 ** power * (num % 2)
        num //= 2
        power += 1
    print(binnum,"")