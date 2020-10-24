def junta_listas(lista_grande):
    i = 0
    lista_simples = []
    while i < len(lista_grande):
        lista_simples += lista_grande[i]
        i += 1
    return lista_simples