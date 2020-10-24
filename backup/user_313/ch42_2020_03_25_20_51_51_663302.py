a = True
lista = []
contador = 0

while a:
    b = input('Digite uma palavra: ')
    palavra = b
    lista.append(palavra)
    contador = contador + 1
 
    if b == 'fim':
        a = False
        del lista[contador-1]
        #print(lista)

i = 0
a = True
d = len(lista)


while i < d:
    palavra = lista[i]
    if len(palavra) > 0 and palavra[0] == 'a':
        print(palavra)
    i = i + 1