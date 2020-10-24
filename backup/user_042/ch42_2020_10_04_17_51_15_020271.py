lista_palavras = [] 
palavra = input('Palavra?')

while palavra != 'fim':
    lista_palavras.append(palavra)
    palavra = input('Outra palavra?')
#Imprime apenas palavras que começam com a 
i = 0 
while i < len(lista_paalavras):
    palavra = lsita_palavras[i]
    if len(palavra) > 1 and palavra[0] == 'a':
        print (palavra)
    i +=1