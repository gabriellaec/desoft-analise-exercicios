def zera_negativos(lista):
    i = 0
    soma = 0
    while i < len(lista):
        soma = lista[i] + lista[i+1]
        i += 1