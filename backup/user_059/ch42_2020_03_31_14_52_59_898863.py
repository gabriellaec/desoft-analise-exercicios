lista = []
while True:
    x = input('Digite uma palavra: ')
    if x!='fim':
        if x[0]=='a':
            lista.append(x)
        else:
            pass
    else: 
        break
i = 0
while i<len(lista): 
    print(lista[i])
    i+=1
