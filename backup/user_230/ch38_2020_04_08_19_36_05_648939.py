def quantos_uns(n):
    quant=0
    n=str(n)
    for i in n:
        if i=="1":
            quant+=1
            return quant
    