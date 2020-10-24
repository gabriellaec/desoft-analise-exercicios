# Importa biblioteca
import numpy as np

# Define função
def encontra_maximo(matriz):
    nova_lista = []             # Lista com elementos da matriz
    valores_absolutos = []      # Lista com módulos dos elementos
    for lista in matriz:
        # Converte matriz em lista
        for numero in lista:
            nova_lista.append(numero)
    # Encontra máximo absoluto e retorna
    maximo = max(nova_lista)
    return maximo