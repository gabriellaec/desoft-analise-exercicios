lista_palavras=[]
digite = input('Digite uma palavra: ')
while digite != 'fim':
    lista_palavras.append(digite)
    digite = input('Digite uma palavra: ')   
x = 0 
#i = 0
while x<len(lista_palavras):
    palavra = lista_palavras[x]
    primeiro_a = palavra[0]
    if primeiro_a == 'a':
        print(palavra)
    #i += 1
    x += 1
    


	

    