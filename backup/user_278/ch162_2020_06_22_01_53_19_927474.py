def verifica_lista(lista):
    if lista == []:
        return 'misturado'
    else:
        for i in lista:
            if i%2==0:
                while i<len(lista):
                    i+=1
                    if lista[i] %2==0:
                        return 'par'
                        i+=1
                    else:
                        return 'misturado'
                        break
            else:
                while i<len(lista):
                    i+=1
                    if lista[i] %2!=0:
                        return 'ímpar'
                        i+=1
                    else:
                        return 'misturado'
                        break
                