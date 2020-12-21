print("Select program")
print("1. Navodit's Binary and Decimal Calculator")
p = int(input("What program do you want to run:"))


if p == 1:
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    c = int(input("What is your choice:"))
    if c == 1:
        import bin2dec
        bin2dec.bin2dec()
    if c == 2:
        import dec2bin
        dec2bin.dec2bin()