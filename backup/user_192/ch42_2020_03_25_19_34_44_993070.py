lista = []
i = 0 
lista.append (input('Qual o numero? '))
while lista[i] != 'fim':
	lista.append (input('Qual o numero? '))
    i += 1
                      
k = 0 
while k < len(lista):
	primeira_letra = lista[k][0]
    if primeira_letra == 'a':
        print(lista[k])
    k += 1
