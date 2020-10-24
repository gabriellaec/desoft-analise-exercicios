def verifica_progressao (lista_razao, lista_quociente):
    for r,q in lista_razao, lista_quociente:
        if r == razao:
            resultado ='PA'
        if q == quociente:
            resultado ='PG'
        if r == q:
            resultado ='AG'
        else:
            resultado ='NA'
    return resultado

print (verifica_progressao(lista_razao, lista_quociente))