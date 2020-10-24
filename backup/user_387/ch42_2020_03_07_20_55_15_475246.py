lista = []
palav = 0


while palav != "fim":

    palav = str(input('Palavra :'))
    lista.insert(0, palav)

for palavra in lista:
    if palavra[0] == 'a':
        print(palavra)