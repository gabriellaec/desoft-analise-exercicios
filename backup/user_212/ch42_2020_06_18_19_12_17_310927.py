palavra = str(input("Digite uma palavra"))

lista = []
while palavra != 'fim':
    lista.append(palavra)
    palavra = str(input("Digite uma palavra"))

i=0
while i < len(lista):
    if lista[i][0] == 'a':
        print(lista[i])
        
    i += 1
    