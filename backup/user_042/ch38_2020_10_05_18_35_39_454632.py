def quantos_uns(n):
    i = 0
    quantos_1 = 0
    while i == len(n) :
        if n[0:i] == 1:
            quantos_1 += 1
            i += 1
        else: 
            i += 1