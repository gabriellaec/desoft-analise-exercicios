def calcula_total_da_nota(lista1,lista2):
        i = 0
        lista3 = []*len(lista1)
        soma = 0
        while i < len(lista1):
            lista3.append(lista1[i] * lista2[i])
            soma += lista3[i]
            i = i + 1
        return soma