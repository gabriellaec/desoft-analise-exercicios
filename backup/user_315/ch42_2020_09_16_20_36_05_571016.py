lista = []

pergunta = input ('Insira uma palavra: ')
lista.append (pergunta)

while lista[-1] != 'fim': 
    
    pergunta = input ('Insira uma palavra: ')
    lista.append (pergunta)

i = 0
while i < len(lista):
    if lista [i][0] == 'a':
        print (lista[i])
    i += 1 