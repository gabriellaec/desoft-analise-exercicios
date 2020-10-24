lista = []
palavra_nova = 'sim'
i=0
while palavra_nova != 'fim':
    lista.append(input('adicione uma palavra na lista: '))
    palavra_nova = lista[i]
    i = i+1

N = len(lista)    
I = 0    
while I<N:
    palavra = lista[I]
    if palavra[0] == 'a':
        print(palavra)
    I = I+1    
    
  
