lista_palavras = []
palavra= input('Escreva uma palavra: ')
while palavra != 'fim':
    lista_palavras.append(palavra)
    palavra= input('Escreva outra palavra: ')
    
i=0
while i<len(lista_palavras):
    palavra=lista_palavras[i]
    if len(palavra) > 1 and palavra[0] == 'a':   
    	i+=1
		print (palavra)


    
    