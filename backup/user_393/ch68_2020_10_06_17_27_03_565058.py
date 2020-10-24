def separa_trios(nomes):
    trios= []
    n= 0
    while n < len(nomes):
        trios.append(nomes[n:n+3])
        n= n + 3
    return trios
