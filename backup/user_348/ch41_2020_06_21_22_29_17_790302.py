def zera_negativos(valores):
    i = 0
    while i < len(valores):
        # Verifica se o elemento atual é negativo
        if valores[i] < 0:
            # Atualiza o elemento do índice para 0
            valores[i] = 0
        i = i + 1
    return valores  
        
