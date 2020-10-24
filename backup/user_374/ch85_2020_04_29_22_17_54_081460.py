def conta_palavras(teste):
    with open(teste, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
         
        i = 0
        print(palavras)
        for p in palavras:
            if p.lower()  == 'banana':
                i += 1            
            if p.lower()  == 'banana.':
                i += 1
        return i        
print(conta_palavras('macacos-me-mordam.txt'))