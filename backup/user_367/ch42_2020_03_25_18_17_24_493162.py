lista = []
palavra = input('digite uma palavra  ')
while palavra != 'fim':
    lista.append(palavra)
    palavra = input('outra palavra ')
    i = 0
	while i < len(lista):
    	palavra = lista[i]
    if len(palavra) > 0 and palavra[0] == 'a':
        print(palavra)
    i += 1