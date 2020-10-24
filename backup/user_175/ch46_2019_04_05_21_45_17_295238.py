lista1 = []

palavra1 = input('Digite uma palavra:')
while palavra1 != 'fim':
        lista1.append(palavra1)
        palavra1 = input('Digite uma palavra:')
    
i = 0
while i < len(lista1):
    palavra2 = lista1[i]
    if palavra2[0] == 'a' and len(palavra2) > 1:
        print(palavra2)
    i += 1