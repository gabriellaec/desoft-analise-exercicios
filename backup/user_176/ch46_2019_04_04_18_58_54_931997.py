lista = []
palavra = input('digite uma palavra: ')
while palavra != 'fim':
    lista.append(palavra)
    palavra = input('digite uma palavra: ')
    
i= 0 
while i < len(lista):
    if lista[i][0] == 'a': #lista[i][0] -> primeiro valor da primeira palavra da lsita
        print(lista[i])
    i+=1
    