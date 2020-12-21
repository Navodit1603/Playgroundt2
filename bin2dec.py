def bin2dec():
    num = int(input("Binary Number: "))
    dec=0
    power=0
    while num > 0:
        dec += 2 ** power * (num % 10)
        num //= 10
        power += 1
    print(dec,"")