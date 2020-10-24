def separa_trios(lista):
    N=3
    liste=[lista[n:n+N] for n in range(0, len(lista),N)]
    return liste