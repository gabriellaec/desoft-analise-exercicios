lista = []
i = 0

while len(lista) < 99:
    if x==1 or x==0:
        i = i + 1
        print('Nao eh primo')
    elif x==2:
        lista = lista.append(i)
        i = i + 1
    elif x>1:
        if x%2==0:
            print('divisivel por 2')
        else:
            y=3
            a=True
            while a:
                if x>y and x%y==0:
                    print('NAO')
                elif x==y:
                    lista = lista.append(i)
                    i = i+1
                    a=False
                y=y+2