def verifica_progressao(lista):
    for numeros in lista:
        if lista[numeros +1] - lista[numeros] == lista[numeros+2] - lista[numeros+1]:
            return "PA"
        elif lista[numeros +1]/lista[numeros] == lista[numeros+2]/lista[numeros+1]:
            return "PG"
        elif lista[numeros +1] - lista[numeros] == lista[numeros+2] - lista[numeros+1] and lista[numeros +1]/lista[numeros] == lista[numeros+2]/lista[numeros+1]:
            return "AG"
        else:
            return "NA"