invalid=True
lista=[]
while invalid:
    palavra = str(input('palavra:'))
    prim_letra=palavra[0]
	if prim_letra == 'a':
    	lista.append(palavra)
    	print(palavra)
    if palavra == 'fim':
        invalid= False
        print(lista[])
        