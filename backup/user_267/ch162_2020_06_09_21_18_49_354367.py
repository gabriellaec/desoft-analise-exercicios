def verifica_lista(l):
    for i in l:
        if l == []:
            return 'misturado'
        elif i%2 != 0:
            return 'ímpar'
        elif i%2 == 0:
            return 'par'
        else:
            return 'misturado'           
   