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
    # Lista com valores absolutos
    for numero in nova_lista:
        numero = np.abs(numero) 
        valores_absolutos.append(numero)
    # Encontra máximo absoluto e retorna
    maximo = max(valores_absolutos)
    return maximo