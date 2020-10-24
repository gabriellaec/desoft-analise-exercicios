def equaliza_imagem (Lista_n, K):
    
    for c in range(len(Lista_n)):
        Lista_n[c] = Lista_n[c]*K
        if Lista_n[c] > 255:
            Lista_n[c] = 255
            
    return Lista_n      