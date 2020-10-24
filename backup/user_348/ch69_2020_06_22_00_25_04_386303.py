def junta_listas (lista):
    # Cria a lista simples
    lista_simples = []
    # Determina o índice atual
    i = 0
    while i < len(lista):
        # Soma a lista simples à lista do índice
        lista_simples = lista_simples + lista[i]
        i = i + 1
    return lista_simples