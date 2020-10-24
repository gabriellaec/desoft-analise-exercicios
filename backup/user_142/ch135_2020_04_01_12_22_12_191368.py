def equaliza_imagem (Lista, K):
    i = 0
    while i in (len(Lista)):
        Lista[l] = Lista[l]*K
        if Lista[l] > 255:
            Lista[l] = 255
            i = i + 1
    return Lista       