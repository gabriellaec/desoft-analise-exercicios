lista = []
Y = True
while Y:
    palavra = input('Digite uma palavra ')

    if palavra == 'fim':
        Y = False
    else:
        lista.append(palavra)

for i in lista:
    if i[0].lower() == 'a':
        print(i)
     
     