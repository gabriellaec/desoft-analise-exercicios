lista_palavras=[]
lista_palavras=(input('Digite uma palavra: '))
while lista_palavras != 'fim':
	lista_palavras.append (input('Digite uma palavra: '))

x = 0 
i = 0
while x<len(lista_palavras):
    palavra = lista_palavras[i]
    primeiro_a = palavra[0]
    if primeiro_a == 'a':
        print(palavra)
    i += 1
    x = x+1
    


	

    