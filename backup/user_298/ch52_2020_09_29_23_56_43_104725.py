precos = []
quant = []
def calcula_total_da_nota(precos,quant):
    t = 0
    total = 0
    while t < len(precos):
        a = precos[t]*quant[t]
        total += a
        t += 1

    return total