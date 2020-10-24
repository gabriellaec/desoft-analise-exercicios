def  classifica_lista(numeros):
    i = 0
    while len(numeros) >= 2:
        elif numeros[i+1] > numeros[i]:
            i += 1
            return 'crescente'
        elif numeros[i+1] < numeros[i]:
            i += 1
            return 'decrescente'
        else:
            i += 1
            return 'nenhum'
        