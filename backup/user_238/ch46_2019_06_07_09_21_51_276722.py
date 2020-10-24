palavra='oi'
lista = []
while palavra != str('fim'):
    palavra=input('palavra: ')
    lista.append(palavra)
for palavra in lista:
    if palavra[0] == 'a':
    print(palavra)
    