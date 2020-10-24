lista = []

pergunta = input ('Insira uma palavra: ')
lista.append (pergunta)

x = 0 
while lista[x] != 'fim': 
    
    pergunta = input ('Insira uma palavra: ')
    lista.append (pergunta)
    x += 1

i = 0
while i < len(lista):
    if lista [i][0] == 'a':
        print (lista[i])
    i += 1 