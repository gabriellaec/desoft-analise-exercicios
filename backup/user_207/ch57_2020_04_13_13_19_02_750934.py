
def verifica_progressao (lista):
    razao = lista[i+1] - lista[i]
    quociente = lista[i+1]/lista[i]
    
    resultado = ''

    i=0
    while i+2 <len(lista):

        if razao == lista[i+2] - lista[i+1]:
            resultado = 'PA'
        elif quociente == lista[i+2]/lista[i+1]:
            resultado = 'PG'
        elif razao == lista[i+2] - lista[i+1] and quociente == lista[i+2]/lista[i+1]:
            resultado = 'AG'
        else:
            resultado = 'NA'
        i+=1
    return resultado