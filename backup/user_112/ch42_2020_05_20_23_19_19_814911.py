palavra = True
lista = []

while palavra:
    n = input('palavra: ')
    
    if n != 'fim':
        lista.append(n)
    else:
        for x in lista:
            if x[0] == 'a': 
                print(x) 
        palavra = False

