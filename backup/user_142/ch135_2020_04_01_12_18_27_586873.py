def equaliza_imagem (Lista, K):
    i = 0
    while i in (len(Lista)):
        Lista[i] = Lista[i]*K
        if Lista[i] > 255:
            Lista[i] = 255
            i = i + 1
    return Lista       