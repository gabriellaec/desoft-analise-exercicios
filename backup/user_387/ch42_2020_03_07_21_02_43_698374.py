lista = []
palav = 0


while palav != "fim":

    palav = str(input('Palavra :'))

    if palav == 'fim':
        break
    
    else:
        lista.insert(0, palav)

for palavra in lista:
    if palavra[0] == 'a' or palavra[0] == 'A':
        print(palavra)