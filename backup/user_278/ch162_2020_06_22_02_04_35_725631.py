def verifica_lista(lista):
    if lista == []:
        return 'misturado'
    for i in range(len(lista)):
        if lista[i]%2==0 and lista[-1]%2==0:
            return 'par'
        if lista[i]%2!=0 and lista[-1]%2!=0:
            return 'ímpar'
        else:
            return 'misturado'