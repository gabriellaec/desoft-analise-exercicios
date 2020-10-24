lista = []
i = 0
lista.append(input('Qual é a palavra: '))
while lista[i] != 'fim':
    i += 1
    lista.append(input('Qual é a palavra: '))
x = 0
N = len(lista)
while x<N:
    if lista[x][0] == 'a':
        print(lista[x])
        x += 1
    else:
        x += 1
   


	


    

    
	