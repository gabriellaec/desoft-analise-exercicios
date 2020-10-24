with open ('macacos-me-mordam.txt','r') as textinho:
    palavras = textinho.read()
    bananas = [] 
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra == 'banana':
            bananas.append(palavra)
print(len(bananas))
            