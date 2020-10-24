def junta_listas (lista):
    lista_simples = []
    for i in lista:
        numero = lista[i] + lista[i + 1] 
        lista_simples.append(numero)
    return lista_simples