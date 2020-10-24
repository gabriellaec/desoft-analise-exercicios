lista = []
acabou = True
while acabou:
    a = input('palavras: ')
    lista.append(a)
    a = input("mais um?")
    if a == 'fim':
        acabou = False
print(calcula_norma(lista))