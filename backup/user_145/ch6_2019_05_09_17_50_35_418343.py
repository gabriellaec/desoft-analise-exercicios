'''Escreva uma função que recebe uma matriz de tamanho 3×3
e devolve o maior valor absoluto dentre todos os seus elementos. A matriz é representada por uma lista de listas. Exemplo: a lista [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
representa a matriz:
																	⎛1 2 3⎞
																	⎜4 5 6⎟
																	⎝7 8 9⎠

Curiosidade: o maior valor absoluto encontrado em uma matriz é conhecido como a norma infinito dessa matriz.
O nome da sua função deve ser encontra_maximo.'''


def encontra_maximo(matriz):
    maior = 0
    for lista in matriz:
        for e in lista:
            if e > maior:
                maior = e
    return maior
z = [[1, 2, 3], [-10], [7, 8, -9]]
print(encontra_maximo(z))