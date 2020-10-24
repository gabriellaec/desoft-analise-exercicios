with open('macacos-me-mordam.txt','r') as arquivo:
    texto = arquivo.read()
    
dados = json.loads(texto)

print(len(dados)