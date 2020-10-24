def equaliza_imagem (Lista, K):
    while i in (len(Lista)):
        i = 0
        Lista[i] = Lista[i]*K
        if Lista[i] > 255:
            Lista[i] = 255
            i = i + 1
    return Lista       