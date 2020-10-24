def junta_listas(lista_externa):
    lista_junta = []
    for lista_interna in lista_externa:
        for valores in lista_interna:
            lista_junta.append(valores)
    return lista_junta