lista = []
while 'fim' not in lista:
    palavras = input('Digite palavra: ')
    lista.append(palavras)

i = 0
while i < len(lista):
    if 'a' == lista[i][0]:   
        print(lista[i])
        i += 1
    else:
        i += 1