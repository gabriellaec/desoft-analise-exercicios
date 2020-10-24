def verifica_lista(l1):
    if l1 == '':
        return 'misturado'
    else:
        for i in l1:
            if i%2==0:
                while i < len(l1):
                    if i%2==0:
                        continue
                    else:
                        return 'misturado'
                return 'par'
                
            elif i%2!=0:
                while i < len(l1):
                    if i%2!=0:
                        continue
                    else:
                        return 'misturado'
                return 'impar'
                    