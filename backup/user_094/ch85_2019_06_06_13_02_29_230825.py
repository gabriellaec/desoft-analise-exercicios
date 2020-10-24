with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    
    i=0
    if 'banana' in conteudo.lower():
        i+=1
    return i