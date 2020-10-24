def equaliza_imagem (Lista, K):
    
    for c in range(len(Lista)):
        Lista[c] = Lista[c]*K
        if Lista[c] > 255:
            Lista[c] = 255
            
    return Lista       