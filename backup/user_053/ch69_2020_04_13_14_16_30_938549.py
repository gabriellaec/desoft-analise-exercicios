def junta_listas(lista_composta):
    lista_simples = []
    # Varre lista composta
    for lista in lista_composta:
        # Adiciona à lista simples cada elemento da lista interna
        for elemento in lista:
            lista_simples.append(elemento)
    return lista_simples