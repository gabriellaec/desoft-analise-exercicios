def verifica_primos(lista):
    dic = {}
    for i in lista:
        div = 0
        tam = range(2,len(lista)+1)
        for a in tam:
            if i % a == 0:
                div += 1
        if div >= 2:
            #print(f'{i} é divisivel {div} vezes')
            dic[i] = True
        else:
            #print(f'{i} é primo')
            dic[i] = False
    return dic
	