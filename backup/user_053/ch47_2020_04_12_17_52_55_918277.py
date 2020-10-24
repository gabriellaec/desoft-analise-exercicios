# Define função
def estritamente_crescente(lista):
    lista_crescente = []    # Lista de retorno
    contador = 0            # Conta o índice do último elemento da nova lista
    if len(lista) > 0:
        # Adiciona o primeiro elemento da lista
        lista_crescente.append(lista[0])
        # Percorre a lista e adiciona os números em sequência crescente
        for i in range (0, len(lista)):
            if lista[i] > lista_crescente[contador]:
                lista_crescente.append(lista[i])
                contador += 1
    # Retorna lista crescente
    return lista_crescente