def verifica_lista(lista):
    lista = []
    for i in lista:
        if i%2 != 0:
            return 'impar'
        elif i%2 == 0:
            return 'par'
        else:        
            return 'misturado'        