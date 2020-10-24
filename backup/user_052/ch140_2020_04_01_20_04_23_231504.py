def faixa_notas (lista):
    lista1 = 0
    lista2 = 0
    lista3 = 0
    for x in lista:
        if x < 5:
            lista1 +=1
        elif x <= 7:
            lista2 +=1
        else:
            lista3 +=1
    resultado = [lista1,lista2,lista3]
    return resultado
            
    