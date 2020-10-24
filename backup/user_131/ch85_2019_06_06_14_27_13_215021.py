with open('macacos-me-mordam.txt','r') as arquivo: 
    conteudo = arquivo.read()

novo_conteudo = conteudo.upper()

n = novo_conteudo.count("BANANA")
        
print(n)

