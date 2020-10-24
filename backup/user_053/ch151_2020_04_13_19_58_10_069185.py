def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        # Verifica se é crescente
        contador = 0
        for i in range(0, len(lista) - 1):
            if lista[i+1] > lista[i]:
                contador += 1
            else:
                i = len(lista)
        if contador == len(lista) - 1:
            return 'crescente'
        else:
            # Verifica se é decrescente
            contador = 0
            for j in range(0, len(lista) - 1):
                if lista[j+1] < lista[j]:
                    contador += 1
                else:
                    j = len(lista)
            if contador == len(lista) - 1:
                return 'decrescente'
            else:
                return 'nenhum'