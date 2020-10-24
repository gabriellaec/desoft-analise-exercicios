def eh_crescente(n):
    condicao = True
    i = 1
    while condicao == True and i < len(n):
        if n[i] > n[i-1]:
            condicao = True
            i = i + 1
        else:
            condicao  = False
    return condicao