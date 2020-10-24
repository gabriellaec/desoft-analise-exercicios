lista_vazia=[]
palavra = input('Digite uma palavra: ')
if palavra[0] == 'a':
    lista_vazia.append(palavra)
elif palavra == 'fim':
    print(lista_vazia)

while palavra != 'fim':
    palavra = input('Digite uma palavra: ')
    if palavra[0] == 'a':
        lista_vazia.append(palavra)
print(lista_vazia)
