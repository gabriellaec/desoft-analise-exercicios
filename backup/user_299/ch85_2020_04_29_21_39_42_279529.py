with open ('macacos-me-mordam.txt','r') as textinho:
    cont = textinho.read()
    palavras = cont.split()
    bananas = [] 
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra == 'banana':
            bananas.append(palavra)
print(len(bananas))
            