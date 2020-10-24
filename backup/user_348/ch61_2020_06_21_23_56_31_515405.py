def filtra_positivos (numeros):
    # Cria uma lista onde serão adicionados os números positivos
    lista = []
    # Determina uma variável onde será lido o índice
    i = 0
    # Determina a condição para o loop
    while i < len(numeros):
        # Verifica se o elemento do índice atual é positivo
        if numeros[i] > 0:
            # Se for adiciona esse elemento à lista de números positivos
            lista.append(numeros[i])
        i = i + 1
    return lista