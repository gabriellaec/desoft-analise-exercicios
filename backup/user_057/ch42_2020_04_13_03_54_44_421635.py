lista = []
i=0
palavra_nova = 'sim'
while palavra_nova != 'fim':
    lista [i] = input('adicione uma palavra na lista: ')
    palavra_nova = lista [i]
    i = i+1

N = len(lista)    
I = 0    
while i<N:
    palavra = lista[I]
    if palavra[0] == 'a':
        print(palavra)
    I = I+1    
    
  
