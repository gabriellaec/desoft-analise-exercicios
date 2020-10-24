arquivo = open("macacos-me-mordam.txt", 'r', encoding="utf8")
cont = 0
for line in arquivo:
    palavras = line.split(' ')
    for palavra in palavras:
        if palavra.lower() == 'banana':
            cont += 1
print(cont)