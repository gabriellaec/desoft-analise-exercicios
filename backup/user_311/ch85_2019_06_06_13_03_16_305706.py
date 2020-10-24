with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    
texto = conteudo.lower()
asd = texto.split()
i = 0
for a in asd:
    if a == "banana":
        i += 1

print(i)
