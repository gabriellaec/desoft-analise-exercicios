
def verifica_progressao (lista):
    razao = lista[-1] - lista[-2]
    quociente = lista[-1]/lista[-2]
    
    resultado = ''

    i=0
    while i+1 <len(lista):

        if razao == lista[i+1] - lista[i]:
            resultado = 'PA'
        elif quociente == lista[i+1]/lista[i]:
            resultado = 'PG'
        elif razao == lista[i+1] - lista[i] and quociente == lista[i+1]/lista[i]:
            resultado = 'AG'
        else:
            resultado = 'NA'
        i+=1
    return resultado