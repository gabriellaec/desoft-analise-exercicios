def eh_crescente(lista_numeros):
    i=0
    maior = 0
    while i < len(lista_numeros):
        if lista_numeros[i] > maior:
            maior = lista_numeros[i]
            if maior > lista_numeros[i]:
                return False
            else:
                return True
        i+=1