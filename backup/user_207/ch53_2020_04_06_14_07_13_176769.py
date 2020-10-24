lista_de_numeros =[]

def soma_impares (lista_de_numeros):
    soma =0
    for e in (lista_de_numeros):
        if e%2 ==1:
            soma += e
    return soma