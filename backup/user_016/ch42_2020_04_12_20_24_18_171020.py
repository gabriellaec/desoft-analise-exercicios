lista = []
exercicio = True
while exercicio:
    x = input('Qual a palavra? ')
    if x[0] == 'a':
        lista.append(x)
        print(x)
    elif x == 'fim':
        break
    else:
        pass
        
    