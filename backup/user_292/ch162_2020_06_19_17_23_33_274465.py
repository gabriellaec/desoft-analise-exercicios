def verifica_lista(l):
    par = 0
    ímpar = 0 
    tamanho_l = len(l)
    for i in l:
        if i % 2 == 0:
            par += 1
        else:
            ímpar += 1
    if tamanho_l == 0:
        return "misturado"
    if tamanho_l == par:
        return "par"
    if tamanho_l == ímpar:
        return "ímpar"
    else:
        return "misturado"
    