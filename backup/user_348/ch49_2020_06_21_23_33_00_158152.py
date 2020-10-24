def inverte_lista (lista):
    # Cria uma lista vazia onde serão adicionados os números invertidos
    invertida = []
    # Determina a variável que será armazenado o índice da lista
    i = len(lista) - 1
    # Determina a condição do loop
    while i >= 0:
        # Adiciona os elementos da lista inicial à lista nova
        invertida.append(lista[i])
        # Como está indo de traz pra frente o i diminui
        i = i - 1
    return invertida