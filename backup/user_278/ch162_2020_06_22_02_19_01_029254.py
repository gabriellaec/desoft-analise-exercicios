def verifica_lista(lista):
    if lista == []:
        return 'misturado'
    verifica = 0
    for i in range(len(lista)):
        if lista[i]%2==0:
            verifica+=0
        else:
            verifica+=1
    if verifica==0:
        return 'par'
    elif verifica == len(lista):
        return 'ímpar'
    else:
        return 'misturado'