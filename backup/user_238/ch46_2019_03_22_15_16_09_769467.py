palavra=input('palavra: ')
lista = []
while palavra != str('fim'):
    if palavra[0] == 'a':
    	lista.append(palavra)
    palavra=input('palavra: ')
print(lista)
