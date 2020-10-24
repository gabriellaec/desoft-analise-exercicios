# Define função
def encontra_maximo(matriz):
    nova_lista = []             # Lista com elementos da matriz

    for lista in matriz:
        # Converte matriz em lista
        for numero in lista:
            nova_lista.append(numero)

    # Encontra máximo absoluto e retorna
    maximo = max(nova_lista)
    return maximo