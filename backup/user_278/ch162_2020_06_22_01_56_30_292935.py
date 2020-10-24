def verifica_lista(lista):
    if lista == []:
        return 'misturado'
    else:
        for i in lista:
            if i%2==0:
                while i<len(lista):
                    if lista[i]%2==0:
                        return 'par'
                    else:
                        return 'misturado'
                        break
                    i+=1
            else:
                while i<len(lista):
                    if lista[i]%2!=0:
                        return 'ímpar'
                    else:
                        return 'misturado'
                        break
                    i+=1
                