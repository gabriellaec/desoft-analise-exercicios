lista_palavras = [] 
palavra = input('Palavra?')

while palavra != 'fim':
    lista_palavras.append(palavra)
    palavra = input('Outra palavra?')
    
#Imprime apenas palavras que começam com a 
i = 0 
while i < len(lista_palavras):
    palavras = lista_palavras[i]
    if len(palavras) > 1 and palavras[0] == 'a':
        print (palavras)
    i +=1