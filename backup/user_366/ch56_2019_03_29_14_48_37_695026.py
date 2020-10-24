def calcula_total_da_nota(precos, qtde):
    i = 0 
    s = 0
    while i < len(precos):
        a = precos[i] * qtde[i]
        s += a
        i += 1
    return s