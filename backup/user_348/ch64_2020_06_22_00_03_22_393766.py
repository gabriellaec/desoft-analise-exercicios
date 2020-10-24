def acha_bigramas (string):
    # Cria uma lista onde serão adicionados ps bigramas
    lista = []
    # Define o loop
    for i in range(len(string)-1):
        # Cria uma variável que determina o que é um bigrama
        bigrama = string[i] + string[i + 1]
        # Verifica se o bigrama criado já tá na lista de bigramas
        if not bigrama in lista:
            # Se não tiver é adicionado
            lista.append(bigrama)
    return lista
    