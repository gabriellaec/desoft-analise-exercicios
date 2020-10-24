def verifica_progressao (lista):    
    resultado = ''
    examinar = True

    i=0
    while examinar and i+2 <len(lista):
        razao = lista[1] - lista[0]
        quociente = lista[1]/lista[0]

        if razao == lista[i+2] - lista[i+1]:
            resultado = 'PA'
        elif quociente == lista[i+2]/lista[i+1]:
            resultado = 'PG'
        elif razao == lista[i+2] - lista[i+1] and quociente == lista[i+2]/lista[i+1]:
            resultado = 'AG'
        else:
            resultado = 'NA'
            examinar = False   
        i+=1
    return resultado
