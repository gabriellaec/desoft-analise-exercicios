def monta_mala(lista_antes):
    i=len(lista_antes)-1
    while sum(lista_antes)>23:
        lista_antes-=lista_antes[i]
        i-=1
    return lista_antes